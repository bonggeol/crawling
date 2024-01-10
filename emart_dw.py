import requests
from bs4 import BeautifulSoup
import time

url = "https://emart.ssg.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
}

response = requests.get(url, headers=headers)
print(f"response: {response}")
soup = BeautifulSoup(response.text, "html.parser")
print(f"soup: {soup}")
links = soup.select(
    "#skip_gnb > div > div.emgnb_ctg > div > div > ul > li > a")
print("시작")
print(f"links: {links}")

for link in links:
    print("link")
    href = link["href"]
    full_url = url + href
    print("--------------------------------------------------------------")
    print(f"URL: {full_url}")

    page = 1
    while True:
        print("while 들어옴")
        response = requests.get(full_url + "&page={}".format(page))
        print(f"response: {response}")
        print(full_url + "&page={}".format(page))
        time.sleep(3)
        soup = BeautifulSoup(response.text, "html.parser")
        products = soup.select("#ty_thmb_view > ul > li")
        # print(f"products: {products}")

        if not products:
            break

        for product in products:
            print("--------------------------------------------------------------")
            product_name = product.select_one(
                "div.mnemitem_tit > span.mnemitem_goods_tit"
            ).text.strip()
            product_cata = link.text.strip()
            product_price = product.select_one(
                "div.mnemitem_pricewrap_v2 > div.mnemitem_price_row > div > em"
            ).text.strip()
            unit_price = product.select_one(
                "div.mnemitem_pricewrap_v2 > div.unit_price"
            )
            if unit_price:
                unit_price = unit_price.text.strip()
            else:
                unit_price = "가격 없음"
            print(f"상품 이름: {product_name}")
            print(f"카테고리: {product_cata}")
            print(f"상품 가격: {product_price}")
            print(f"단위당 가격: {unit_price}")
        page += 1
        time.sleep(1)
