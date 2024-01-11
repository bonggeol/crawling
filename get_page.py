import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import re


def get_page(url):
    # Setup chrome options
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


    # Choose Chrome Browser
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    # wait loading
    # time.sleep(1)

    # 카테고리별 total page 불러오기
    page = driver.find_element(By.CLASS_NAME, 'paging')
    last_page = page.find_element(By.CLASS_NAME, 'btn_last')
    total_page_str = last_page.get_attribute('onclick')

    tmp_page = re.search(r'\((\d+)\)', total_page_str)
    total_page = int(tmp_page.group(1)) if tmp_page else None

    driver.quit()
    return total_page
