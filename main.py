from crawler import LinksCrawler
from utils import *

if __name__ == "__main__":

    ancher_text = 'laptop'

    target = int(input(f'''{200 * '*'}
    1.Torob
    2.Basalam
    3.Torob and Basalam
    Please choice "Target" : '''))
    print(200 * '*')

    if target == 1:
        target_name = 'Torob.com'
        crawler = LinksCrawler(ancher_text)
        html_doc = crawler.get_page_source(TOROB)
        data = crawler.find_data(html_doc, TOROB_TITLE_CLASS, TOROB_PRICE_CLASS, TOROB_TITLE_TAG, TOROB_PRICE_TAG)

        for title, price in zip(data[0], data[1]):
            print(f"Title: {title.text}\t", f"Price: {price.text}")

    if target == 2:
        target_name = 'Basalam.com'
        crawler = LinksCrawler(ancher_text)
        html_doc = crawler.get_page_source(BASALAM)
        data = crawler.find_data(
            html_doc, BASALAM_TITLE_CLASS, BASALAM_PRICE_CLASS, BASALAM_TITLE_TAG, BASALAM_PRICE_TAG
        )

        for title, price in zip(data[0], data[1]):
            print(title.text, price.text)

    if target == 3:

        crawler = LinksCrawler(ancher_text)

        html_doc = crawler.get_page_source(TOROB)
        data_torob = crawler.find_data(html_doc, TOROB_TITLE_CLASS, TOROB_PRICE_CLASS, TOROB_TITLE_TAG, TOROB_PRICE_TAG)

        html_doc = crawler.get_page_source(BASALAM)
        data_basalam = crawler.find_data(
            html_doc, BASALAM_TITLE_CLASS, BASALAM_PRICE_CLASS, BASALAM_TITLE_TAG, BASALAM_PRICE_TAG
        )

        print("Torob.com")
        for title, price in zip(data_torob[0], data_torob[1]):
            print(f"Title: {title.text}\t", f"Price: {price.text}")

        print(40 * "*")

        print("Basalam.com")
        for title, price in zip(data_basalam[0], data_basalam[1]):
            print(f"Title: {title.text}\t", f"Price: {price.text}")
