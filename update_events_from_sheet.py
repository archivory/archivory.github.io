import requests
import csv
from datetime import datetime
import shutil
import os
import re

def parse_event_date(date_str):
    # Try to parse various date formats, fallback to a low value if not parseable
    fmts = ["%B %d, %Y", "%B %d, %y", "%B %d", "%Y-%m-%d"]
    for fmt in fmts:
        try:
            # If year is missing, infer year: if date is in the future, use previous year
            if fmt == "%B %d" and "," not in date_str:
                today = datetime.now()
                try_date = datetime.strptime(f"{date_str}, {today.year}", "%B %d, %Y")
                if try_date > today:
                    try_date = datetime.strptime(f"{date_str}, {today.year-1}", "%B %d, %Y")
                return try_date
            return datetime.strptime(date_str.strip(), fmt)
        except Exception:
            continue
    return datetime.min

# Google Sheet info
gsheet_id = '1D5V7A367ItJy7YMdEhYUhVsELiFRTVXSAMTb519KKJ8'
sheet_name = 'Events' 
csv_url = f'https://docs.google.com/spreadsheets/d/1D5V7A367ItJy7YMdEhYUhVsELiFRTVXSAMTb519KKJ8/gviz/tq?tqx=out:csv&sheet=Events'
response = requests.get(csv_url)
response.raise_for_status()

md_path = 'events.md'
backup_path = md_path + '.bak'
if os.path.exists(md_path):
    shutil.copy(md_path, backup_path)
    print(f'Backup created: {backup_path}')
with open(md_path, 'r') as f:
    md_content = f.read()

# Fetch events from Google Sheet
lines = response.text.splitlines()
reader = csv.DictReader(lines)
sheet_events = list(reader)
print('Fetched events from Google Sheet:')
for event in sheet_events:
    print(event)

def events_table(events):
    if not events:
        return 'No events.'
    table = '\n| Date | Title | Location | Description |\n|------|-------|----------|-------------|\n'
    for e in events:
        desc = e.get('Description','')
        desc = desc.replace('\n', ' ')
        table += f"| {e.get('Date','')} | {e.get('Title','')} | {e.get('Location','')} | {desc} |\n"
    table += '\n'
    return table

events_md = events_table(sorted(sheet_events, key=lambda x: parse_event_date(x.get('Date', '')), reverse=True))

def replace_between(text, start_marker, end_marker, new_content):
    pattern = re.compile(rf'({re.escape(start_marker)})(.*?)(\s*{re.escape(end_marker)})', re.DOTALL)
    if pattern.search(text):
        return pattern.sub(rf'\1\n{new_content}\3', text)
    else:
        return None

if ('<!-- BEGIN EVENTS -->' in md_content and '<!-- END EVENTS -->' in md_content):
    new_md = replace_between(md_content, '<!-- BEGIN EVENTS -->', '<!-- END EVENTS -->', events_md)
    if new_md is not None:
        front_matter_match = re.match(r'(?s)^---.*?---\s*', md_content)
        if front_matter_match:
            front_matter = front_matter_match.group(0)
            new_md_no_front = re.sub(r'(?s)^---.*?---\s*', '', new_md)
            final_md = front_matter + new_md_no_front
        else:
            final_md = new_md
        with open(md_path, 'w') as f:
            f.write(final_md)
        print('Events page updated between markers from Google Sheet, front matter preserved.')
    else:
        print('ERROR: Markers not found. No changes made.')
        if os.path.exists(backup_path):
            shutil.copy(backup_path, md_path)
            print('Restored events page from backup.')
else:
    print('ERROR: Required marker comments not found. No changes made.')
    if os.path.exists(backup_path):
        shutil.copy(backup_path, md_path)
        print('Restored events page from backup.')
