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
        print(f"DBNAME: {DBNAME}")
        print(f"HOSTNAME: {HOSTNAME}")
        print(f"USERNAME: {USERNAME}")
        print(f"PASSWORD: {PASSWORD}")
        print(f"PORT: {PORT}")
        conn = psycopg2.connect(host = HOSTNAME, dbname= DBNAME, user = USERNAME, password = PASSWORD, port = PORT)
        print("Connection successful")
        return conn
    except:
        print("Postgres not connected")
        exit()


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

def get_product_id(product_name: str):
    product_id_query = '''SELECT id FROM products WHERE products.product_name = (%s) LIMIT 1;'''
    cur.execute(product_id_query, (product_name, ))
    id = cur.fetchone()
    return str(id[0])


def get_product_from_id(id: str):
    product_name_query = ''' SELECT product_name FROM products WHERE products.id = (%s) LIMIT 1;'''
    cur.execute(product_name_query, (id, ))
    product_name = cur.fetchone()
    return product_name[0]


def get_product_prices(product_name: str):
    product_prices_query = ''' SELECT price, scraped_time FROM products WHERE products.product_name = (%s) ORDER BY scraped_time;'''
    cur.execute(product_prices_query, (product_name, ))
    product_prices = cur.fetchall()
    return product_prices

conn = connection()
create_table(conn)
if not conn:
    print("Postgres not connected")
    exit()
    
print("Postgres connected")
cur = conn.cursor()
