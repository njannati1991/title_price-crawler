from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from utils import *
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep


class LinksCrawler:

    def __init__(self, ancher_text):
        self.ancher_text = ancher_text
        self.target_links = TOROB
        self.title_selector = {'torob_title': TOROB_TITLE_CLASS}
        self.price_selector = {'torob_price': TOROB_PRICE_CLASS}

    def get_data(self):

        driver = webdriver.Chrome()
        driver.get(self.target_links)
        driver.implicitly_wait(1)

        for _ in range(20):
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)

        html_doc = driver.page_source

        driver.quit()

        return html_doc

    def find_data(self):

        html_doc = self.get_data()
        soup = BeautifulSoup(html_doc, 'html.parser')
        titles = soup.find_all('h2', class_=self.title_selector['torob_title'])
        prices = soup.find_all('div', class_=self.price_selector['torob_price'])

        return titles, prices
