TOROB = "https://torob.com/search/?query="
BASALAM = "https://basalam.com/s?q="


TOROB_TITLE_CLASS = "jsx-9e6201846c11ef54 product-name"
TOROB_PRICE_CLASS = "jsx-9e6201846c11ef54 product-price-text"
TOROB_TITLE_TAG = 'h2'
TOROB_PRICE_TAG = 'div'

BASALAM_TITLE_CLASS = "_5PwYIn Sh2LgL"
BASALAM_PRICE_CLASS = "_oC9ho"
BASALAM_TITLE_TAG = 'a'
BASALAM_PRICE_TAG = 'span'

























#
# data = []
# for link, class_name in zip(self.target_links, self.class_name):
#     option = webdriver.ChromeOptions()
#     option.add_argument('--headless')
#     driver = webdriver.Chrome(options=option)
#     driver.get(link + self.ancher_text)
#     driver.implicitly_wait(10)
#     links = []
#     while len(links) < 30:
#         product_elements = driver.find_elements(By.CLASS_NAME, class_name)
#
#         for element in product_elements:
#             html_element = element.get_attribute("outerHTML")
#             soup = BeautifulSoup(html_element, 'html.parser')
#             link = soup.find('a')
#             if link and link.get('href'):
#                 links.append(link.get('href'))
#
#         driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
#     data.append(links)
# return data