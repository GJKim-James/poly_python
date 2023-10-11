import urllib.request
import bs4

url = "https://www.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")  # BeautifulSoup은 데이터를 추출하는데 필요한 기능이 들어 있는 파싱 라이브러리
# 파싱하기 위해서 BeautifulSoup에 데이터를 넣은 후 파이썬에서 가공할 수 있는 형태로 만들줌.

top_right = bs_obj.find("div", {"class": "service_area"})

print(top_right)

first_a = top_right.find("a")  # a 태그를 찾아서 first_a에 저장

print(first_a.text)  # first_a.text로 a 태그 안에 있는 text만 추출
