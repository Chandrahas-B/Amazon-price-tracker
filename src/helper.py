def get_price_from_string(price: str):
    price = price.replace(',', '')
    price = price[1:]
    return int(price)

def get_time_from_datetime(time):  # datatype of time is datetime
    time = str(time)
    time = time.split('.')
    return time[0]

def get_price_and_time(prices_and_scrapedTimes: list):
    prices = []
    scraped_times = []
    for price, scraped_time in prices_and_scrapedTimes:
        prices.append(get_price_from_string(price))
        scraped_times.append(get_time_from_datetime(scraped_time))
    return prices, scraped_times