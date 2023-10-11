import urllib.request  # 웹의 특정 주소로 요청을 보내는 기능

url = "https://www.naver.com/"
html = urllib.request.urlopen(url)  # 텍스트 형식으로 네이버 페이지를 호출한 데이터가 문자열 형태로 저장
# html : <http.client.HTTPResponse object at 0x0000021DFCE544A8>

print(html.read())
