from bs4 import BeautifulSoup
import requests

def get_page(url: str):
    HEADERS = {
        'User-Agent': ('Mozilla/5.0 (X11; Linux x86_64)'
                        'AppleWebKit/537.36 (KHTML, like Gecko)'
                        'Chrome/44.0.2403.157 Safari/537.36'),
        'Accept-Language': 'en-US, en;q=0.5'
        }

    html_page = requests.get(url, headers= HEADERS)
    content = BeautifulSoup(html_page.content, 'html5lib')
    product_list = get_results(content)
    return product_list


def get_results(content):
    product_list = {}
    urls = {}
    for div_blocks in content.find_all('div', {'data-asin': lambda x: x and x.startswith('B0')}):
        products =  div_blocks.find_all('span', {'class': 'a-size-base-plus a-color-base a-text-normal'})
        if len(products) == 0:
            products =  div_blocks.find_all('span', {'class': 'a-size-medium a-color-base a-text-normal'})
        prices = div_blocks.find_all('span', {'class': 'a-offscreen'})
        url = div_blocks.find_all('a', {'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style', 'target': '_blank'})
        if len(url):
            url = url[0]['href']
            url = 'https://www.amazon.in'+ str(url)
        for product, price in zip(products, prices):
            product_list[product.string] = price.string
            if len(url):
                urls[product.string] = url
        if len(product_list) == 5:
            break
    return product_list, urls


# async def get_product(product_div):
#     # Query for all elements at once
#     image_element_future = product_div.query_selector('img.s-image')
#     name_element_future = product_div.query_selector(
#         'h2 a span')
#     price_element_future = product_div.query_selector('span.a-offscreen')
#     url_element_future = product_div.query_selector(
#         'a.a-link-normal.s-no-hover.s-underline-text.s-underline-link-text.s-link-style.a-text-normal')