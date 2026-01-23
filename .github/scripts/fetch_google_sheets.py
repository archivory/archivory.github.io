import gspread
import os
import pandas as pd
from google.oauth2.service_account import Credentials

# Define the scopes required for Google Sheets and Drive API
SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

# Function to fetch Google Sheets data and save as a CSV
def fetch_google_sheets_as_csv(sheet_id, range_name, output_csv_path):
    creds = None
    # Load credentials from a JSON key file stored in GitHub Secrets
    creds_info = {
        "type": "service_account",
        "project_id": os.getenv("GOOGLE_PROJECT_ID"),
        "private_key_id": os.getenv("GOOGLE_PRIVATE_KEY_ID"),
        "private_key": os.getenv("GOOGLE_PRIVATE_KEY").replace("\n", "\n"),
        "client_email": os.getenv("GOOGLE_CLIENT_EMAIL"),
        "client_id": os.getenv("GOOGLE_CLIENT_ID"),
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": os.getenv("GOOGLE_CLIENT_X509_CERT_URL")
    }

    creds = Credentials.from_service_account_info(creds_info, scopes=SCOPES)
    
    # Connect to Google Sheets API
    gc = gspread.authorize(creds)
    sheet = gc.open_by_key(sheet_id)

    # Select the first worksheet
    worksheet = sheet.worksheet(range_name)
    
    # Get all records in the sheet
    records = worksheet.get_all_records()

    # Convert records to DataFrame and save as CSV
    df = pd.DataFrame(records)
    df.to_csv(output_csv_path, index=False)

if __name__ == "__main__":
    # Define parameters of the script
    SHEET_ID = os.getenv("GOOGLE_SHEET_ID")  # Add your sheet ID to GitHub Secrets
    RANGE_NAME = os.getenv("GOOGLE_SHEET_RANGE")  # Specify the sheet tab name
    OUTPUT_CSV_PATH = "_data/sheet_data.csv"  # Path where the CSV file will be stored

    print("Fetching data from Google Sheets...")
    fetch_google_sheets_as_csv(SHEET_ID, RANGE_NAME, OUTPUT_CSV_PATH)
    print(f"Google Sheets data saved to {OUTPUT_CSV_PATH}")