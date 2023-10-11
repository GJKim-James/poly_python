import os
import sys
import urllib.request
import datetime
import time
import json

client_id = 'ciQGk4NmMyu10qErVgvf'
client_secret = 'JkKhThhK68'


# [CODE 1]
def getRequestUrl(url):
    req = urllib.request.Request(url)  # 매개변수인 url에 대한 요청을 보낼 객체 생성
    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)

    try:
        response = urllib.request.urlopen(req)  # 요청 객체를 보내고 응답을 받아 response 객체에 저장
        if response.getcode() == 200:  # getcode()로 response 객체에 저장된 코드 확인
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None


# [CODE 2]
def getNaverSearch(node, srcText, start, display):
    base = "https://openapi.naver.com/v1/search"
    node = "/%s.json" % node
    parameters = "?query=%s&start=%s&display=%s" % (urllib.parse.quote(srcText), start, display)

    url = base + node + parameters

    responseDecode = getRequestUrl(url)  # [CODE 1]
    # 완성한 url을 이용하여 getRequestUrl() 함수를 호출하여 받은 utf-8 디코드 응답을 responseDecode에 저장

    if responseDecode == None:
        return None
    else:
        return json.loads(responseDecode)  # 서버에서 받은 JSON 형태의 응답 객체를 파이썬 객체로 로드하여 반환


# [CODE 3]
def getPostData(post, jsonResult, cnt):
    title = post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']

    pDate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900')
    pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')

    jsonResult.append({'cnt': cnt, 'title': title, 'description': description,
                       'org_link': org_link, 'link': org_link, 'pDate': pDate})
    return


# [CODE 0]
def main():
    node = 'news'  # 크롤링할 대상
    srcText = input('검색어를 입력하세요 : ')
    cnt = 0
    jsonResult = []

    jsonResponse = getNaverSearch(node, srcText, 1, 100)  # [CODE 2]
    total = jsonResponse['total']

    while (jsonResponse != None) and (jsonResponse['display'] != 0):
        for post in jsonResponse['items']:
            cnt += 1
            getPostData(post, jsonResult, cnt)  # [CODE 3]

        start = jsonResponse['start'] + jsonResponse['display']
        jsonResponse = getNaverSearch(node, srcText, start, 100)  # [CODE 2]

    print("전체 검색 : %d건" % total)

    with open("%s_naver_%s.json" % (srcText, node), 'w', encoding='utf-8') as outfile:
        jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)

        outfile.write(jsonFile)

    print("가져온 데이터 : %d건" % cnt)
    print("%s_naver_%s.json SAVED" % (srcText, node))


if __name__ == '__main__':
    main()
