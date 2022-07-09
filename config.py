from selenium import webdriver

DIRECTORY = 'reports'
NAME = 'Laptops'
CURRENCY = '₹'
MIN_PRICE = '60000'
MAX_PRICE = '150000'
FILTERS = {
    'min': MIN_PRICE,
    'max': MAX_PRICE
}
BASE_URL = "http://www.amazon.in/"
CHROME_OPTIONS = ['--ignore-certificate-errors', '--incognito', '--headless']


def get_chrome_web_driver(options):
    return webdriver.Chrome("./chromedriver", chrome_options=options)


def get_web_driver_options():
    return webdriver.ChromeOptions()


def set_chrome_options(options, *args):
    for arg in args:
        options.add_argument(arg)
