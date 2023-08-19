from bs4 import BeautifulSoup
import sqlite3
import requests

def get_page(url: str):
    # try:
    html_page = requests.get(url)
    
    return html_page