from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from utils import *
from selenium import webdriver
from bs4 import BeautifulSoup


class LinksCrawler:

    def __init__(self, ancher_text):
        self.ancher_text = ancher_text

    def get_page_source(self, target):

        driver = webdriver.Chrome()
        driver.get(target + self.ancher_text)
        driver.implicitly_wait(1)

        for _ in range(20):
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)

        html_doc = driver.page_source
        driver.quit()

        return html_doc

    def find_data(self, html_doc, title_selector, price_selector, title_tag, price_tag):

        soup = BeautifulSoup(html_doc, 'html.parser')
        titles = soup.find_all(title_tag, class_=title_selector)
        prices = soup.find_all(price_tag, class_=price_selector)

        return titles, prices
