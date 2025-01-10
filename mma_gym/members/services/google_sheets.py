import gspread
from google.oauth2.service_account import Credentials
from django.conf import settings

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Initialize Google Sheets client


def get_google_sheet():
    credentials = Credentials.from_service_account_file(
        settings.GOOGLE_SHEETS_KEY_FILE, scopes=SCOPES
    )
    client = gspread.authorize(credentials)
    sheet = client.open_by_key(settings.SHEET_ID)
    return sheet


def get_all_members():
    """Fetch all member records."""
    sheet = get_google_sheet().sheet1
    return sheet.get_all_records()


def add_member(data):
    """Add a new member."""
    sheet = get_google_sheet().sheet1
    sheet.append_row(data)


def update_member(row, column, value):
    """Update a specific cell for a member."""
    sheet = get_google_sheet().sheet1
    sheet.update_cell(row, column, value)


def delete_member(row):
    """Delete a member by row."""
    sheet = get_google_sheet().sheet1
    sheet.delete_rows(row)
