from TikTokGet import TikTokGet_Meta
import json

contas = ["@luara", "@paulomuzy", "@dodyaquino", "@anitta"]

for conta in contas:
    data = TikTokGet_Meta(conta)
    
    with open(f"./coleta/{data['Collection_date']}_{data['Brand']}.json", "w") as write_file:
        json.dump(data, write_file, indent=4)
