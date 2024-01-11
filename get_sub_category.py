import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def get_sub_category(big_category_url):
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


    # Choose Chrome Browser
    driver = webdriver.Chrome(options=chrome_options)

    # category_url = 'https://emart.ssg.com/disp/category.ssg?dispCtgId=6000213114'
    driver.get(big_category_url)

    # wait loading
    time.sleep(1)

    top_category = driver.find_element(By.CLASS_NAME, 'emall_category_slider')
    all_category = top_category.find_elements(By.TAG_NAME, 'li')
    category_url_list = []

    for li in all_category:
        atag = li.find_element(By.TAG_NAME, 'a')
        href = atag.get_attribute('href')
        category_url_list.append(href)

    driver.quit()
    return category_url_list
