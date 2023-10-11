from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime


# [CODE 1]
def hollys_store(result):
    for page in range(1, 58):
        Hollys_url = 'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=%d&sido=&gugun=&store=' % page
        print("Hollys_url :", Hollys_url)
        html = urllib.request.urlopen(Hollys_url)
        soupHollys = BeautifulSoup(html, 'html.parser')
        tag_tbody = soupHollys.find('tbody')
        for store in tag_tbody.find_all('tr'):
            if len(store) <= 3:  # 57페이지 '등록된 지점이 없습니다.' 부분
                break
            store_td = store.find_all('td')
            store_name = store_td[1].string
            store_sido = store_td[0].string
            store_address = store_td[3].string
            store_phone = store_td[5].string
            result.append([store_name] + [store_sido] + [store_address] + [store_phone])
    return


# [CODE 0] - 크롤링한 데이터 저장하기
def main():
    result = []
    print('Hollys store crawling >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    hollys_store(result)  # [CODE 1] 호출
    hollys_tbl = pd.DataFrame(result, columns=('store', 'sido-gu', 'address', 'phone'))
    # DataFrame? 테이블 형태(엑셀 모양)로 이루어진 데이터프레임
    hollys_tbl.to_csv('./hollys.csv', encoding='cp949', mode='w', index=True)  # 테이블(데이터프레임)을 csv 파일로 저장
    del result[:]


if __name__ == '__main__':
    main()
