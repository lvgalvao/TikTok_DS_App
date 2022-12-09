import psycopg2
import json
from config import USER, PASSWORD
from glob import glob

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
        followers VARCHAR(255),
        following VARCHAR(255),
        likes VARCHAR(255),
        collection_date DATE
    )
""")

# insert data into the table
for file in glob('./coleta/*.json'):
    with open(file) as f:
        data = json.load(f)
        cur.execute("""
                INSERT INTO instagram_data (brand, followers, following, likes, collection_date)
                VALUES (%s, %s, %s, %s, %s)
            """, (
                data['Brand'],
                data['Followers'],
                data['Following'],
                data['Likes'],
                data['Collection_date']
            ))

# commit the changes
conn.commit()

# close the connection
conn.close()