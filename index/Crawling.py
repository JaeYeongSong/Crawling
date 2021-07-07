from bs4 import BeautifulSoup
import requests
import sys
import time

# 홈페이지 주소 가져오기
url = "https://xsop.tistory.com/category"

tm = time.localtime()

# 현재 시간 (년, 월, 일, 시, 분) 함수 만들기
now_year_real = (tm.tm_year)
now_mon_real = (tm.tm_mon)
now_day_real = (tm.tm_mday)
now_hour_real = (tm.tm_hour)
now_min_real = (tm.tm_min)

# 문자 앞에 0 추가하는 작업
now_year = str(now_year_real).zfill(2)
now_mon = str(now_mon_real).zfill(2)
now_day = str(now_day_real).zfill(2)
now_hour = str(now_hour_real).zfill(2)
now_min = str(now_min_real).zfill(2)

html = requests.get(url)
bs_html = BeautifulSoup(html.content, "html.parser")
bsObject = bs_html.find_all(attrs={"class":"name"})

now_ymdhm = now_year + '-' + now_mon + '-' + now_day + ' ' + now_hour + '시' + ' ' + now_min + '분'

sys.stdout = open(f'D:/list/{now_ymdhm}.txt', 'w', encoding='UTF-8')

print(bsObject) # 웹 페이지 txt 파일로 출력