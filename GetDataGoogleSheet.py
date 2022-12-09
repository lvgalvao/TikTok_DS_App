class GetDataGoogleSheet:
    def __init__(self, sheet_name, range_name):
        self.sheet_name = sheet_name
        self.range_name = range_name

    def get_data(self):
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
        client = gspread.authorize(creds)
        sheet = client.open(self.sheet_name).sheet1
        data = sheet.get_all_records()
        return data