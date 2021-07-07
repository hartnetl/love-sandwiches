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

# Below checks API is working. Not needed once checked, delete in normal file
# sales = SHEET.worksheet('sales')  # Access 'sales' worksheet data in our spreadsheet
# data = sales.get_all_values()  # get_all_values is a gspread method
# print(data)

def get_sales_data():
    """
    Get sales figures input from user
    """
    print("Please enter sales data from the last market.")
    print("Data should be six numbers, separated by commas.")
    print("Example: 10,20,30,40,50,60\n")

    data_str = input("Enter your data here: ")
    print(f"The data provided here is {data_str}")

get_sales_data()