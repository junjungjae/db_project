# 공공데이터 포탈로부터 원하는 태그의 데이터를 받아옴
import requests
from bs4 import BeautifulSoup

dust_open_api_key = 'serviceKey=x1KWB7efKVqWTlOiMb58bvC%2BOfCUWS%2BkeklhD9Nd6TFUW4NtL07ObtmOYg%2BCKvMl6nX%2BMQBlyD7j4IaL405rSw%3D%3D'
dust_params = '&numOfRows=100&pageNo=1&sidoName=경기&searchCondition=DAILY'
dust_open_url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureSidoLIst?' + dust_open_api_key + dust_params


res = requests.get(dust_open_url)

matter = BeautifulSoup(res.content, 'lxml')

data = matter.find_all('item')

for item in data:
    dosx = item.find('cityname')
    if dosx is None:
        continue
    else:
        print(dosx)


