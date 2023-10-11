from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime

from selenium import webdriver
import time


# [CODE 1]
def CoffeeBean_store(result):
    CoffeeBean_URL = "https://www.coffeebeankorea.com/store/store.asp"
    wd = webdriver.Chrome('./webdriver/chromedriver.exe')  # 크롬 webdriver 객체 생성

    for i in range(1, 250):  # 매장 수 만큼 반복(몇 개인지 몰라서 대략 250으로 정함)
        wd.get(CoffeeBean_URL)  # 웹 페이지 연결
        time.sleep(1)  # 웹페이지 연결할 동안 1초 대기
        try:
            wd.execute_script("storePop2(%d)" % i)  # 매장 정보 페이지를 열기 위해 자바스크립트 함수인 storePop() 호출
            time.sleep(1)  # 스크립트 실행할 동안 1초 대기
            html = wd.page_source  # 자바스크립트가 수행된 페이지의 소스코드 저장
            soupCB = BeautifulSoup(html, 'html.parser')  # BeautifulSoup 객체 생성
            store_name_h2 = soupCB.select("div.store_txt > h2")  # 매장 이름 추출
            store_name = store_name_h2[0].string
            print("{} 매장명 : ".format(i), store_name)  # 매장 이름 출력하기
            store_info = soupCB.select("div.store_txt > table.store_table > tbody > tr > td")  # 매장 주소 추출
            print("list(store_info[2] : ", list(store_info[2]))
            store_address_list = list(store_info[2])
            store_address = store_address_list[0]
            store_phone = store_info[3].string  # 매장 전화번호 추출
            result.append([store_name] + [store_address] + [store_phone])
        except:
            continue
    return


# [CODE 0] - 크롤링한 데이터 저장하기
def main():
    result = []
    print('CoffeeBean store crawling >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    CoffeeBean_store(result)  # [CODE 1] 호출

    CB_tbl = pd.DataFrame(result, columns=('store', 'address', 'phone'))
    CB_tbl.to_csv('./CoffeeBean.csv', encoding='cp949', mode='w', index=True)


if __name__ == '__main__':
    main()
