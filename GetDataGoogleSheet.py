import gspread

credentials = {
    "web": {
        "client_id": "922107450968-f5926l8gnbpumkl315cc7udl8h0s7rj8.apps.googleusercontent.com",
        "project_id": "website-253001",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_secret": "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"
    }
}

gc, authorized_user = gspread.oauth_from_dict(credentials)

sh = gc.open("Example spreadsheet")

print(sh.sheet1.get('A1'))