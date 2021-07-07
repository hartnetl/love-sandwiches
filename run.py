import gspread
from google.oauth2.service_account import Credentials

SCOPE = [  # SCOPE is written in caps to tell other developers its a const variable, do not change
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')  # parameter is the name of our spreadsheet doc

sales = SHEET.worksheet('sales')  # Access 'sales' worksheet data in our spreadsheet

data = sales.get_all_values()  # get_all_values is a gspread method
print(data)
