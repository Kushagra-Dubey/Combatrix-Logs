
# MMA Gym Management System

This project is a web application for managing MMA gym member registrations, fee tracking, and Google Sheets integration. It uses Django as the backend and integrates Google Sheets as a database to store member details and track their monthly fees.

## Features

- **Member Registration**: Members can fill out a registration form to store their details.
- **Google Sheets Integration**: Member data is stored in Google Sheets and accessed via the Google Sheets API.
- **Fee Tracking**: Monthly fees are tracked using a separate table in Google Sheets, and payment statuses are managed.
- **Admin Interface**: Admin can view and manage the member data and fee statuses from the backend.
- **Frontend Visualization**: A table is displayed on the frontend to view all members and their data.

## Technologies Used

- **Backend**: Django
- **Frontend**: Bootstrap or Tailwind CSS (You can choose whichever you prefer)
- **Database**: Google Sheets
- **APIs**: Google Sheets API for interacting with data
- **Environment Management**: `.env` for managing sensitive data like the service account key

## Prerequisites

- Python 3.x
- Django 3.x or above
- Google Cloud Platform account with a service account key (for Google Sheets API)
- Access to Google Sheets (for storing and retrieving data)

## Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/your-username/mma-gym-management.git
cd mma-gym-management
```

### Step 2: Install Dependencies

First, create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

- On **Windows**:
  ```bash
  venv\Scriptsctivate
  ```
- On **Mac/Linux**:
  ```bash
  source venv/bin/activate
  ```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Step 3: Set Up Google Sheets API

1. Go to the **Google Cloud Console** and create a new project or select an existing one.
2. Enable the **Google Sheets API** and **Google Drive API** for your project.
3. Create a **Service Account** and download the `.json` key file.
4. Add the email from the Service Account (which can be found in the JSON file) as an editor to your Google Sheets document.

### Step 4: Create a `.env` File

In the root of the project (same level as `manage.py`), create a `.env` file and add the following variables:

```env
GOOGLE_SERVICE_ACCOUNT_KEY_PATH=service_account_key.json
SHEET_ID=your_google_sheet_id
```

Replace `service_account_key.json` with the actual file name of your service account key and `your_google_sheet_id` with the ID of the Google Sheet you want to use.

### Step 5: Run the Django Server

Apply migrations:

```bash
python manage.py migrate
```

Run the server:

```bash
python manage.py runserver
```

Your application should now be running at `http://127.0.0.1:8000/`.

## Usage

1. **Member Registration**: Members can fill out the registration form, which will save their details to Google Sheets.
2. **Admin Panel**: Admins can view the table of members and track their monthly fees.
3. **Frontend**: The members' data is displayed on a webpage with a table layout.

## Folder Structure

```
mma_gym_management/
│
├── .env                      # Environment variables (e.g., service account key and sheet ID)
├── manage.py                 # Django's manage script
├── mma_gym/                  # Django project folder
│   ├── __init__.py
│   ├── settings.py           # Django settings file
│   ├── urls.py
│   └── ...
└── members/                  # App folder (handles member-related functionality)
    ├── migrations/
    ├── models.py             # Model definitions (if applicable)
    ├── views.py              # Views for handling registration and data display
    ├── templates/
    │   └── members_table.html # HTML template for displaying member data
    └── ...
```

## Notes

- The `.env` file should be kept private and not committed to version control. Add it to `.gitignore`.
- This setup uses Google Sheets as a "database" for storing member information and fee data. Ensure that the Service Account has the necessary permissions to access and modify the Google Sheets.

## Troubleshooting

- **Google Sheets API errors**: Make sure that the Google Sheets API is enabled and the service account has access to the sheet.
- **Missing environment variables**: Ensure that the `.env` file is present in the root directory and that the paths to the service account key and the sheet ID are correct.
