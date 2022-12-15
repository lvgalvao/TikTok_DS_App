import gspread
from gspread_config import SPREADSHEETS, WORKSHEET

class GoogleSheet:
    def __init__(self, sheet_name):
        self.sheet_name = sheet_name
        self.scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        self.sa = gspread.service_account(filename="app/gspread/service_account.json")
        self.sh = self.sa.open(SPREADSHEETS)
        self.sheet = self.sh.worksheet(WORKSHEET)
        

    def get_row(self, row_number):
        return self.sheet.row_values(row_number)

    def get_all_rows(self):
        return self.sheet.get_all_values()

    def get_column(self, column_number):
        return self.sheet.col_values(column_number)

    def get_all_columns(self):
        return self.sheet.get