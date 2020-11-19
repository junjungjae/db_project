# 1일차 : 공공데이터 포탈로부터 원하는 태그의 데이터를 받아옴
# 2일차 : 받아온 데이터를 생성한 db에 저장(weather 컬럼은 임시로 데이터 삽입)
from datetime import datetime
import requests
import pymysql
from bs4 import BeautifulSoup
from flask import json
import urllib

dust_open_api_key = 'serviceKey=x1KWB7efKVqWTlOiMb58bvC%2BOfCUWS%2BkeklhD9Nd6TFUW4NtL07ObtmOYg%2BCKvMl6nX%2BMQBlyD7j4IaL405rSw%3D%3D'
dust_params = '&numOfRows=30&pageNo=1&itemCode=PM10&dataGubun=DAILY&searchCondition=MONTH'
dust_open_url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureLIst?' + dust_open_api_key + dust_params
seoul_url = 'http://api.openweathermap.org/data/2.5/weather?id=1835847&appid=e5e08ba5684c7bf39dcf0310bf5b98ed'




res = requests.get(dust_open_url)
matter = BeautifulSoup(res.content, 'lxml')
tag = matter.td
dateinfo = []
dustvalue = []

#req = urllib.request.urlopen(seoul_url)
#res = req.readline()
#weatherdata = json.loads(res)

conn = pymysql.connect(host='localhost', user='root', password='smile1996', db='dbprac', charset='utf8')
cursor = conn.cursor()


dustdata = matter.find_all('item')
datacnt = 0
for item in dustdata:
    seoul_dust = item.find('seoul').text
    recvdate = item.find('datatime').text
    print(recvdate, seoul_dust)
    sql = '''INSERT INTO seoul (date, dustvalue, weather) VALUES(%s, %s, %s)'''
    cursor.execute(sql, (recvdate, seoul_dust, 'sunny'))

conn.commit()
conn.close()



