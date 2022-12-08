import psycopg2
import json
from config import USER, PASSWORD
# connect to the database
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user=USER,
    password=PASSWORD
)

# create a cursor
cur = conn.cursor()

# create a table
cur.execute("""
    CREATE TABLE IF NOT EXISTS instagram_data (
        brand VARCHAR(255),
        followers INTEGER,
        following INTEGER,
        likes INTEGER,
        collection_date DATE
    )
""")

# insert data into the table
with open('coleta/2022-12-08_@anitta.json') as f:
    data = json.load(f)
    for item in data:
        cur.execute("""
            INSERT INTO instagram_data (brand, followers, following, likes, collection_date)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            item['Brand'],
            item['Followers'],
            item['Following'],
            item['Likes'],
            item['Collection_date']
        ))

# commit the changes
conn.commit()

# close the connection
conn.close()