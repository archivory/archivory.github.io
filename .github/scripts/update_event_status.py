import pandas as pd
from datetime import datetime, timezone

def update_event_status(csv_path):
    # Read the CSV into a pandas DataFrame
    df = pd.read_csv(csv_path)

    # Ensure the column names are standardized for processing
    required_columns = ['start', 'end', 'title', 'location', 'description', 'link', 'image', 'image_alt', 'pinned', 'status']
    if not set(required_columns).issubset(df.columns):
        print(f"Error: CSV is missing required columns. Needs {required_columns}")
        return False

    # Get the current date
    today = datetime.now(timezone.utc).date()

    # Process the rows: move items to 'past' status if their 'end' date has passed
    for index, row in df.iterrows():
        try:
            end_date = datetime.strptime(row['end'], '%Y-%m-%d').date()
            if end_date < today:
                df.at[index, 'status'] = 'past'
            else:
                df.at[index, 'status'] = 'upcoming'
        except ValueError:
            print(f"Warning: Skipping row {index} due to invalid date format in end column.")

    # Save the updated CSV
    df.to_csv(csv_path, index=False)
    print(f"Updated event statuses saved to {csv_path} successfully.")

if __name__ == "__main__":
    CSV_PATH = "_data/sheet_data.csv"  # The relative path to the CSV file in the repository

    print("Updating event statuses based on their 'end' date...")
    update_event_status(CSV_PATH)
    print("Event statuses updated successfully!")