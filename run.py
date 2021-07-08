import gspread
from google.oauth2.service_account import Credentials
# from pprint import pprint

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
    Get sales figures input from user.
    Run a while loop to collect a valid string of data from the user via
    the terminal, which must be a string of 6 numbers separated by commas. The
    loop will repeatedly request data untl it is valid.
    """
    # Create a while loop to ask for data until it's correctly entered
    while True:
        print("Please enter sales data from the last market.")
        print("Data should be six numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60\n")  # Add \n to give more space in the terminal

        data_str = input("Enter your data here please: \n")
        # print(f"The data provided here is {data_str}") <- Use to test fctn is working, then delete

        # To check input data is valid, we must covert data to list of values
        sales_data = data_str.split(",")
        # the split() method returns the broken up values as a list. Here they're broken at the commas.
        # a list like this is returned => ['1', '2', '3', '4', '5', '6', '6']
        # print(sales_data)

        if validate_data(sales_data):
            # if there are no errors, True is returned from validate_data and the below runs and loop is stopped.
            # If there is an error, the code will begin again thanks to the while loop.
            print("Data is valid!")
            break
    return sales_data


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
        return False

    return True
    # returning true or false for get_sales_data above

# THE BELOW SHOULD BE DELETED
# IT WAS REFACTORED TO UPDATE WORKSHEET FUNCTION
# def update_sales_worksheet(data):
#     """
#     Update sales worksheet, add new row with the list data provided
#     """
#     print("updating sales worksheet...\n")
#     # Adding this print gives feedback to user while task completes
#     # It also helps with debugging, as you'll know if this step was completed
#     sales_worksheet = SHEET.worksheet("sales")
#     sales_worksheet.append_row(data)
#     print("sales worksheet updated successfully.\n")


# def update_surplus_worksheet(surplus_data):
#     """
#     Add a new row of data to the surplus worksheet
#     """
#     print("updating surplus worksheet... \n")
#     surplus_worksheet = SHEET.worksheet("surplus")
#     surplus_worksheet.append_row(surplus_data)
#     print("Surplus worksheet succesfully updated")


def update_worksheet(data, worksheet):
    """
    Receives a list of integers to be inserted into a worksheet
    Update the relevant worksheet with the data provided
    """
    print(f"updating {worksheet} worksheet... \n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated succssfully \n")


def calculate_surplus_data(sales_row):
    """
    Compare sales with stock and calculate the surplus for each item type.

    The surplus is defined as the sales figures subtracted from the stock figure:
    - Positive surplus indicates waste
    - Negative surplus indicates extra made when stock ran out
    """
    print("Calculating surplus data...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    # pprint(stock)  This makes rows easier to read
    stock_row = stock[-1]  # This selects the last value
    print(f"stock row: {stock_row}")
    print(f"sales row: {sales_row}")

    surplus_data = []
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)
    print(f"surplus data: {surplus_data}")
    return surplus_data


def get_last_5_entries_sales():
    """
    Collects columns of data from sales worksheet, collecting the last 5 entries
    for each sandwich and returns the data as a list of lists.
    """
    sales = SHEET.worksheet("sales")
    # column = sales.col_values(3) # this is a gspread method. Index starts at 1
    # print(column)

    columns = []
    for ind in range(1, 7):
        column = sales.col_values(ind)
        columns.append(column[-5:])  # The colon creates the list of lists
    # pprint(columns)

    return columns


def calculate_stock_data(data):
    """
    Calculate the average stock for each item type, adding 10%
    """
    print("calculating stock data...\n")
    new_stock_data = []

    for column in data:
        int_column = [int(num) for num in column]
        average = sum(int_column) / len(int_column)
        # The above denominator could also be 5 here, as that value will never change
        stock_num = average * 1.1   # Add that 10% extra
        new_stock_data.append(round(stock_num))

    print(f" new stock values: {new_stock_data}")
    return new_stock_data


def main():
    """
    Run all program functions
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data]  # list comprehension to turn string into int
    update_worksheet(sales_data, "sales")
    new_surplus_data = calculate_surplus_data(sales_data)
    update_worksheet(new_surplus_data, "surplus")
    sales_columns = get_last_5_entries_sales()
    stock_data = calculate_stock_data(sales_columns)
    update_worksheet(stock_data, "stock")


print("Welcome to Love Sandwiches Data Automation. \n")
main()
