from bs4 import BeautifulSoup
import requests
import sys

# 홈페이지 주소 가져오기
url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=뉴스"

html = requests.get(url)
bs_html = BeautifulSoup(html.content, "html.parser")

print(bs_html) # 웹 페이지 출력
