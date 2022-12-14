from GetDataTikTok import TikTokGet_Meta
from GoogleSheet import GoogleSheet
import PutDataIntoS3
import json
import boto3
from datetime import date, datetime

today = date.today()
hour = datetime.now().day

## Get all values from TiktokBrands.spreadsheets
GS = GoogleSheet(sheet_name="gspread/service_account.json")
CONTAS = GS.get_all_rows()

## Amazon buckets
bucket_name = 'tiktokbrands-bucket'

for conta in CONTAS:
    data = TikTokGet_Meta(conta)
    s3 = boto3.resource('s3')
    json_file = json.dumps(data, indent=4) #json.dump(data, outfile, indent=4)
    s3object = s3.Object('tiktokbrands-bucket', f"{conta}_{today}_{hour}.json")
    s3object.put(Body=(json_file))

