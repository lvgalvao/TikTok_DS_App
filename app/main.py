# main.py

from fastapi import FastAPI
from redis_om import get_redis_connection

app = FastAPI()

redis_db = get_redis_connection(
    host = '0.0.0.0', port='6379'
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

# from GetDataTikTok import TikTokGet_Meta
# from GoogleSheet import GoogleSheet
# import PutDataIntoS3 as PutDataIntoS3
# import json
# import boto3
# from datetime import date, datetime

# today = date.today()
# hour = datetime.now().day

# ## Get all values from TiktokBrands.spreadsheets
# GS = GoogleSheet(sheet_name="app/gspread/service_account.json")
# CONTAS = GS.get_all_rows()

# ## Amazon buckets
# bucket_name = 'tiktokbrands-bucket'

# for conta in CONTAS:
#     print(conta[0])
#     data = TikTokGet_Meta(conta[0])
#     s3 = boto3.resource('s3')
#     json_file = json.dumps(data, indent=4) #json.dump(data, outfile, indent=4)
#     s3object = s3.Object('tiktokbrands-bucket', f"{conta}_{today}_{hour}.json")
#     s3object.put(Body=(json_file))

