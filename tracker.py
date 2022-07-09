import time
from selenium.webdriver.common.keys import Keys
from config import (
    get_web_driver_options,
    get_chrome_web_driver,
    set_chrome_options,
    NAME,
    CURRENCY,
    FILTERS,
    BASE_URL,
    DIRECTORY,
    CHROME_OPTIONS
)
from selenium.common.exceptions import NoSuchElementException
import json
import os
from datetime import datetime


class AmazonProduct:
    base_url = BASE_URL
    currency = CURRENCY

    def __init__(self, asin, driver):
        self.asin = asin
        self.driver = driver

    @classmethod
    def set_class_static_params(cls, base_url=None, currency=None):
        if base_url!=None: cls.base_url = base_url
        if currency!=None: cls.currency = currency

    def get_info(self):
        print(f"Product ID: {self.asin} - getting data...")
        self.make_url()
        self.driver.get(f'{self.url}?language=en_GB')
        time.sleep(2)  # wait to load page
        self.get_title()
        if self.title:
            print("\tTitle =", self.title)
        else:
            print("\tCould not find Title.")
        self.get_seller()
        if self.seller:
            print("\tSeller =", self.seller)
        else:
            print("\tCould not find Seller.")
        self.get_price()
        if self.price:
            print("\tPrice =", self.price)
        else:
            print("\tCould not find Price.")
        if self.price:
            info_dict = {
                'asin': self.asin,
                'url': self.url,
                'title': self.title,
                'seller': self.seller,
                'price': self.price
            }
            return info_dict
        return None

    def get_title(self):
        try:
            self.title = self.driver.find_element('css selector', '#productTitle').get_attribute('innerHTML').strip()
        except Exception as e:
            print(e)
            print(f"Can't get title of a product - {self.driver.current_url}")
            self.title = None

    def get_seller(self):
        try:
            self.seller = self.driver.find_element('css selector', '#bylineInfo').get_attribute('innerHTML').strip()
        except Exception as e:
            print(e)
            print(f"Can't get seller of a product - {self.driver.current_url}")
            self.seller = None

    def get_price(self):
        try:
            self.price = self.driver.find_element('css selector',"span#tp_price_block_total_price_ww span.a-price-whole").get_attribute('innerHTML').strip()
            self.convert_price()
        except Exception as e:
            print(e)
            print(f"Can't get price of a product - {self.driver.current_url}")
            self.price = None

    def make_url(self):
        self.url = self.base_url + 'dp/' + self.asin

    def convert_price(self):
        try:
            self.price = self.price.split("<")[0]
        except Exception as e:
            print("\tEncountered exception", e, "while parsing price.")
        try:
            self.price = self.price.split(",")[0] + self.price.split(",")[1]
        except Exception as e:
            print("\tEncountered exception", e, "while parsing price.")
        self.price = float(self.price)



class Report:
    filters = FILTERS
    base_link = BASE_URL
    currency = CURRENCY

    def __init__(self, title, data):
        self.data = data
        self.title = title

    def create_report(self):
        report = {
            'title': self.title,
            'date': self.get_now(),
            'best_item': self.get_best_item(),
            'currency': self.currency,
            'filters': self.filters,
            'base_link': self.base_link,
            'products': self.data
        }
        print("Creating report...")
        all_reports_path = os.path.join(os.getcwd(), DIRECTORY)
        Report.create_folder(all_reports_path)
        this_report_folder = os.path.join(all_reports_path,self.title)
        Report.create_folder(this_report_folder)
        this_report_path = os.path.join(this_report_folder,f"{'_'.join(self.get_now().split(' '))}.json")
        with open(this_report_path, 'w') as report_file:
            json.dump(report, report_file, indent=2)
        print("Done.")

    @staticmethod
    def create_folder(path):
        if not os.path.exists(path):
            os.mkdir(path)

    @classmethod
    def set_class_static_params(cls, base_url=None, currency=None, filters=None):
        if base_url!=None: cls.base_url = base_url
        if currency!=None: cls.currency = currency
        if filters!=None: cls.filters = filters

    @staticmethod
    def get_now():
        now = datetime.now()
        return now.strftime("%d-%m-%Y %H:%M:%S")

    def get_best_item(self):
        try:
            return sorted(self.data, key=lambda k: k['price'])[0]
        except Exception as e:
            print(e)
            print("Problem with sorting items")
            return None



class AmazonProductIndex:
    base_url = BASE_URL
    filters = FILTERS

    def __init__(self, search_term):
        self.search_term = search_term
        options = get_web_driver_options()
        set_chrome_options(options, *CHROME_OPTIONS)
        print("Opening Chrome...")
        self.driver = get_chrome_web_driver(options)
        if self.filters['min']==None and self.filters['max']==None:
            self.price_filter = ""
        else:
            self.price_filter = "&rh=p_36%3A"
            if self.filters['min']!=None :
                self.price_filter+=f"{self.filters['min']}00"
            self.price_filter+="-"
            if self.filters['max']!=None :
                self.price_filter += f"{self.filters['max']}00"

    @classmethod
    def set_class_static_params(cls, base_url=None, filters=None):
        if base_url!=None: cls.base_url = base_url
        if filters!=None: cls.filters = filters

    def create_index(self):
        print("Starting Script...")
        print(f"Looking for {self.search_term} products...")
        links = self.get_products_links()
        if not links:
            print("Stopped script.")
            exit()
            return
        print(f"Got {len(links)} links to products.")
        print("Finding products...")
        self.products = self.get_products_info(links)
        print(f"Found {len(self.products)} products.")

    def generate_report(self):
        print("Getting info about products...")
        products_info = [product.get_info() for product in self.products]
        products_info = list(filter(lambda prod_info: prod_info!=None, products_info))
        print(f"Got info about {len(self.products)} products.")
        report = Report(self.search_term, products_info)
        report.create_report()
        return

    def get_products_links(self):
        self.driver.get(self.base_url)
        element = self.driver.find_element('css selector', '#twotabsearchtextbox')
        element.send_keys(self.search_term)
        element.send_keys(Keys.ENTER)
        time.sleep(2)  # wait to load page
        self.driver.get(f'{self.driver.current_url}{self.price_filter}')
        print(f"Our url: {self.driver.current_url}")
        time.sleep(2)  # wait to load page
        result_list = self.driver.find_elements('css selector', '.s-result-list')
        links = []
        try:
            results = result_list[1].find_elements('css selector',
                "div div div div div div div div div div h2 a")
            links = [link.get_attribute('href') for link in results]
            return links
        except Exception as e:
            print("Didn't get any products.")
            print(e)
            return links

    def get_asins(self, links):
        return [self.link_to_asin(link) for link in links]

    @staticmethod
    def link_to_asin(product_link):
        return product_link[product_link.find('/dp/') + 4:product_link.find('/ref')]

    def get_products_info(self, links):
        asins = self.get_asins(links)
        products = [AmazonProduct(asin,self.driver) for asin in asins]
        return products

    def __del__(self):
        try:
            print("Closing Chrome.")
            self.driver.quit()
        except:
            pass



if __name__ == '__main__':
    ProductIndex = AmazonProductIndex(NAME)
    AmazonProductIndex.set_class_static_params(base_url=BASE_URL, filters=FILTERS)
    ProductIndex.create_index()
    AmazonProduct.set_class_static_params(base_url=BASE_URL, currency=CURRENCY)
    Report.set_class_static_params(base_url="BASE_URL", currency=CURRENCY, filters=FILTERS)
    ProductIndex.generate_report()
