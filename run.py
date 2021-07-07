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
    print("Example: 10,20,30,40,50,60\n")  # Add \n to give more space in the terminal

    data_str = input("Enter your data here: ")
    # print(f"The data provided here is {data_str}") <- Use to test fctn is working, then delete

    # To check input data is valid, we must covert data to list of values
    sales_data = data_str.split(",")
    # the split() method returns the broken up values as a list. Here they're broken at the commas.
    # a list like this is returned => ['1', '2', '3', '4', '5', '6', '6']
    # print(sales_data)

    validate_data(sales_data)


def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int, or
    if there aren't exactly 6 values
    """
    # print(values)

    try:
        [int(value) for value in values]
        # the above says for each value in values, change value to an integer
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values are required, you provided {len(values)}")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again")


get_sales_data()
