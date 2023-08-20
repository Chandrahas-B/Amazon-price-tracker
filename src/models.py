import psycopg2
import os
from dotenv import load_dotenv


load_dotenv()


def connection():
    try:
        DBNAME = os.getenv('DBNAME')
        HOSTNAME = os.getenv('DB_HOSTNAME')
        USERNAME = os.getenv('DB_USERNAME')
        PASSWORD = os.getenv('DB_PASSWORD')
        PORT = os.getenv('DB_PORT')
        conn = psycopg2.connect(host = HOSTNAME, dbname= DBNAME, user = USERNAME, password = PASSWORD, port = PORT)
        print("Connection successful")
        return conn
    except:
        return False


def create_table(conn):
    create_product_list = ''' CREATE TABLE IF NOT EXISTS products (
                                    id serial PRIMARY KEY,
                                    product_name VARCHAR (200) NOT NULL,
                                    price VARCHAR (50) NOT NULL,
                                    scraped_time TIMESTAMP default (CURRENT_TIMESTAMP AT TIME ZONE 'IST') NOT NULL 
                                    ); '''
    cur = conn.cursor()
    cur.execute(create_product_list)
    conn.commit()
    
    
def insert_products(product_list: dict):
    insert_row = '''INSERT INTO products 
                    (product_name, price) VALUES
                    (%s, %s)'''
    for product in product_list:
        price = product_list[product]
        cur.execute(insert_row, (product, price))
    conn.commit()


conn = connection()
if not conn:
    print("Postgres not connected")
    exit()
cur = conn.cursor()