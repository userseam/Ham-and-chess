import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Cope-spread-sheet')


def get_sales_data():
    """
    Get sales figures input from the user.
    """
    while True:
        print("Please enter sales data from the last market.")
        print("Data should be six numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60\n")

        data_str = input("Enter your data here: ")
    
        sales_data = data_str.split(",")
        validate_data(sales_data)

        if validate_data(sales_data):
            print("data is valid!")
            break
    return sales_data


def validate_data(values):
    """
     Converts all strings values into ints , 
     Raise ValueError if stringscannot be converted into int,
     or if there arent exactly 6 values
    """
    print(values)
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f'Exactly 6 values reqiured , you provided {len(values)}'
            )

    except ValueError as e:
        print(f"invalid data: {e} , pleas try agian. \n ")
        return False

    return True

def update_sales_worksheet(data):
    """
    This is going to be used to update the worksheet with adding a new row with the list data provided 
    """
    print("Uppdating sales worhsheet ... \n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("Sales worksheet update sucsefull")



def main():
    """
    Run all program functions
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_sales_worksheet(sales_data)


print("welcome to the ham and cheese factoru automation")
main()




