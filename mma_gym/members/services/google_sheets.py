import gspread
from google.oauth2.service_account import Credentials
from django.conf import settings

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]


class GoogleSheetsClient:
    def __init__(self):
        """Initialize the Google Sheets client."""
        self.credentials = Credentials.from_service_account_file(
            settings.GOOGLE_SHEETS_KEY_FILE, scopes=SCOPES
        )
        self.client = gspread.authorize(self.credentials)
        self.sheet = self.client.open_by_key(settings.SHEET_ID)

    def get_sheet(self, sheet_name="Sheet1"):
        """Get a sheet by its name."""
        return self.sheet.worksheet(sheet_name)


class Member(GoogleSheetsClient):
    def __init__(self):
        super().__init__()
        self.sheet = self.get_sheet("Sheet1")

    def get_all_members(self):
        """Fetch all member records."""
        return self.sheet.get_all_records()

    def add_member(self, data):
        """Add a new member."""
        self.sheet.append_row(data)

    def update_member(self, row, column, value):
        """Update a specific cell for a member."""
        self.sheet.update_cell(row, column, value)

    def delete_member(self, row):
        """Delete a member by row."""
        self.sheet.delete_rows(row)


class Membership(GoogleSheetsClient):
    def __init__(self):
        super().__init__()
        self.sheet = self.get_sheet("Sheet2") 

    def get_membership_sheet(self):
        """Get the membership sheet."""
        return self.sheet

    def update_membership(self, row, column, value):
        """Update a specific cell for a membership."""
        self.sheet.update_cell(row, column, value)
