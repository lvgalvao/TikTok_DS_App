from GetDataTikTok import TikTokGet_Meta
import PutDataIntoS3
import json
import boto3
from datetime import date

today = date.today()
contas = [
        "@flaviacharallo",
        "@gkay",
        "@farofadagkayvideos",
        "@multishow",
        "@tirullipa",
        "@keyrochaa",
        "@tainacostaxis",
        "@ruivinhademarte",
        "@badmioficial",
        "@lorenaqueiroz",
        "@mcdonalds_br",
        "@apple",
        "@cocacolavn",
        "@cocacola",
        "@samsungbrasil",
        "@samsung",
        "@samsungespana",
        "@toyota",
        "@mcdonalds",
        "@mcdonaldsfrance",
        "@microsoft",
        "@bmw",
        "@disney",
        "@disneyplus",
        "@disneyparks",
        "@disneyplusid",
        "@disneychannel",
        "@nike",
        "@pepsi",
        "@pepsiindia",
    ]
    
bucket_name = 'tiktokbrands-bucket'

for conta in contas:
    data = TikTokGet_Meta(conta)
    s3 = boto3.resource('s3')
    json_file = json.dumps(data, indent=4) #json.dump(data, outfile, indent=4)
    s3object = s3.Object('tiktokbrands-bucket', f"{conta}_{today}.json")
    s3object.put(Body=(json_file))

