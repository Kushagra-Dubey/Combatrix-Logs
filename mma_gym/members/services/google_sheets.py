import gspread
from google.oauth2.service_account import Credentials
from django.conf import settings

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

class GoogleSheetsClient:
    """Handles authentication and Google Sheets client initialization."""
    
    def __init__(self, sheet_index=1):
        """
        Initializes the Google Sheets client.
        - `sheet_index` should be 1 for Sheet1 (members) and 2 for Sheet2 (memberships).
        """
        self.credentials = Credentials.from_service_account_file(
            settings.GOOGLE_SHEETS_KEY_FILE, scopes=SCOPES
        )
        self.client = gspread.authorize(self.credentials)
        self.sheet = self.client.open_by_key(settings.SHEET_ID).get_worksheet(sheet_index - 1)

    def get_all_records(self):
        return self.sheet.get_all_records()

    def append_row(self, data):
        self.sheet.append_row(data)

    def update_cell(self, row, column, value):
        self.sheet.update_cell(row, column, value)

    def delete_row(self, row):
        self.sheet.delete_rows(row)


class Member:
    """Handles member-related operations in Google Sheets."""
    
    def __init__(self):
        self.client = GoogleSheetsClient(sheet_index=1)  # Sheet1 for members

    def get_all_members(self):
        """Fetch all member records."""
        return self.client.get_all_records()

    def add_member(self, data):
        """Add a new member."""
        self.client.append_row(data)

    def update_member(self, row, column, value):
        """Update a specific cell for a member."""
        self.client.update_cell(row, column, value)

    def delete_member(self, row):
        """Delete a member by row."""
        self.client.delete_row(row)
