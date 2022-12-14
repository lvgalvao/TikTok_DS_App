from app.GoogleSheet import GoogleSheet

class TestClassGoogleSheet:
    def test_get_row(self):
        sheet = GoogleSheet('Test')
        assert sheet.get_row(1) == ['1', '2', '3', '4', '5']

    def test_get_all_rows(self):
        sheet = GoogleSheet('Test')
        assert sheet.get_all_rows() == [['1', '2', '3', '4', '5'], ['6', '7', '8', '9', '10']]

    def test_get_column(self):
        sheet = GoogleSheet('Test')
        assert sheet.get_column(1) == ['2', '7']

    def test_get_all_columns(self):
        sheet = GoogleSheet('Test')
        assert sheet.get_all_columns() == [['1', '6'], ['2', '7'], ['3', '8'], ['4', '9'], ['5', '10']]