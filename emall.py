import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from get_big_category import get_big_category
from get_page import get_page

chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("method=" + "GET")
chrome_options.add_argument(
    "user-agent=" + "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.104 Whale/3.13.131.36 Safari/537.36")
chrome_options.add_argument(
    "accept=" + "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9")
chrome_options.add_argument("accept-encoding=" + "gzip, deflate, br")
chrome_options.add_argument("sec-ch-ua-platform=" + "macOS")
chrome_options.add_argument("cookie=" + "PCID=31489593180081104183684; _fbp=fb.1.1644931520418.1544640325; gd1=Y; X-CP-PT-locale=ko_KR; MARKETID=31489593180081104183684; sid=03ae1c0ed61946c19e760cf1a3d9317d808aca8b; x-coupang-origin-region=KOREA; x-coupang-target-market=KR; x-coupang-accept-language=ko_KR;")

# Set path to chrome/chromedriver as per your configuration
chrome_options.binary_location = "/home/bonggeol/chrome-linux64/chrome"
webdriver_service = Service(
    "/home/bonggeol/chromedriver-linux64/chromedriver")

# Choose Chrome Browser
driver = webdriver.Chrome(
    service=webdriver_service, options=chrome_options)

big_category_list = get_big_category()


for big_category_url in big_category_list:
    page_range = get_page(big_category_url)
    for i in range(1, (page_range+1)):
        driver.get(f"{big_category_url}&page={i}")
        element = driver.find_element(By.ID, 'ty_thmb_view')
        ul_element = element.find_element(
            By.CLASS_NAME, 'mnemitem_grid_lst.ty_lst4_w1000.mnemitem_ty_thmb')
        li_elements = ul_element.find_elements(
            By.CLASS_NAME, 'mnemitem_grid_item')
        for li_element in li_elements:
            product = li_element.find_element(By.CLASS_NAME, 'mnemitem_tit')
            price = li_element.find_element(By.CLASS_NAME, 'ssg_price')
            print(product.text + '  ' + price.text)
        print(str(i) + 'page 끝')
