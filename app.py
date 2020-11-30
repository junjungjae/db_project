# 서울, 인천, 부산의 날짜별 미세먼지 수치와 상태를 알려줌.
# 날짜별 평균 값이기 때문에 최신화를 시킬 경우 어제 날짜까지만 갱신이 됨.

from flask import Flask, render_template
import requests
import pymysql
from bs4 import BeautifulSoup
from datetime import datetime

app = Flask(__name__)

dust_open_api_key = 'serviceKey=x1KWB7efKVqWTlOiMb58bvC%2BOfCUWS%2BkeklhD9Nd6TFUW4NtL07ObtmOYg%2BCKvMl6nX%2BMQBlyD7j4IaL405rSw%3D%3D'
dust_params = '&numOfRows=30&pageNo=1&itemCode=PM10&dataGubun=DAILY&searchCondition=MONTH'
dust_url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureLIst?'
dust_open_url = dust_url + dust_open_api_key + dust_params  # 공공데이터 api 자료 접속 url
res = requests.get(dust_open_url)
matter = BeautifulSoup(res.content, 'lxml')
dustdata = matter.find_all('item')  # 받아온 자료들 중 광역시, 수치 등의 항목

global sqlconnectstate  # 현재 db에 접속된 상태인지 확인(0 : 끊김, 1 : 연결됨)
sqlconnectstate = 0
global conn
conn = None
global cursor
cursor = None
thismonth = int(datetime.today().month)


# 페이지 이동 시 다시 홈 화면으로 돌아오기 위한 html 버튼
ReturnButton = '<input type="button" value="뒤로가기" onclick="history.back(-1);"<br>'

# 각 지역의 전체 미세먼지 정보 들어갔을 때 이번달의 미세먼지 정보 페이지로 이동하는 버튼
thismonthseoulbutton = '<form method="POST" action="/seoul/thismonth"><button type="submit">이번달의 미세먼지</br></button></form>'
thismonthbusanbutton = '<form method="POST" action="/busan/thismonth"><button type="submit">이번달의 미세먼지</br></button></form>'
thismonthincheonbutton = '<form method="POST" action="/incheon/thismonth"><button type="submit">이번달의 미세먼지</br></button></form>'


# 처음 시작, 혹은 db 처리로 인해 sql 접속이 끊겼을 경우 접속하는 함수
def activesql():
    global sqlconnectstate
    global cursor
    global conn
    conn = pymysql.connect(host='localhost', user='root', password='smile1996', db='dbprac', charset='utf8')  # 다음과 같은 정보를 통해 sql 접속
    cursor = conn.cursor()
    sqlconnectstate = 1


# 미세먼지 수치를 기반으로 좋음, 보통, 나쁨, 매우나쁨 등의 상태 출력
def dust_state(value):
    temp = ''
    if value <= 30:
        temp = 'good'
    elif value <= 80:
        temp = 'common'
    elif value <= 150:
        temp = 'bad'
    elif value > 150:
        temp = 'verybad'
    return temp

# 메인페이지
@app.route('/')
def mainpage():
    return render_template('mainpage.html')


# 이번달의 서울의 미세먼지 표시
@app.route('/seoul/thismonth', methods=['POST'])
def show_seoul_thismonth():
    global sqlconnectstate
    global cursor
    global conn
    if sqlconnectstate == 0:
        activesql()

    # 이번 달의 미세먼지 정보만 select 하도록 함
    cursor.execute('''SELECT * FROM seoul where datetime like '_____%s___' order by datetime desc''', thismonth) # where 조건에 이번달을 포함하여 select 실행
    items = cursor.fetchall()  # 실행한 sql 명령문의 결과를 저장
    output = ''

    for item in items:
        output += item[0] + '<br>'
        output += str(item[1]) + '<br>'
        output += str(item[2]) + '<br>' + '<br>'
    return ReturnButton + '<br>' + output

# 이번달의 부산의 미세먼지 표시
@app.route('/busan/thismonth', methods=['POST'])
def show_busan_thismonth():
    global sqlconnectstate
    global cursor
    global conn
    if sqlconnectstate == 0:
        activesql()

    cursor.execute('''SELECT * FROM busan where datetime like '_____%s___' order by datetime desc''', thismonth)
    items = cursor.fetchall()  # 실행한 sql 명령문의 결과를 저장
    output = ''

    for item in items:
        output += item[0] + '<br>'  # 날짜
        output += str(item[1]) + '<br>'  # 미세먼지 수치
        output += str(item[2]) + '<br>' + '<br>'  # 미세먼지 상태 정도
    return ReturnButton + '<br>' + output

# 이번달의 인천의 미세먼지 표시
@app.route('/incheon/thismonth', methods=['POST'])
def show_incheon_thismonth():
    global sqlconnectstate
    global cursor
    global conn
    if sqlconnectstate == 0:
        activesql()

    cursor.execute('''SELECT * FROM incheon where datetime like '_____%s___' order by datetime desc''', thismonth)
    items = cursor.fetchall()  # 실행한 sql 명령문의 결과를 저장
    output = ''

    for item in items:
        output += item[0] + '<br>'  # 날짜
        output += str(item[1]) + '<br>'  # 미세먼지 수치
        output += str(item[2]) + '<br>' + '<br>'  # 미세먼지 상태 정도
    return ReturnButton + '<br>' + output


@app.route('/seoul', methods=['POST'])
def show_Dust_seoul():
    global sqlconnectstate
    global cursor
    global conn
    if sqlconnectstate == 0:
        activesql()

    cursor.execute('''SELECT * FROM seoul order by datetime desc''')
    items = cursor.fetchall()  # 실행한 sql 명령문의 결과를 저장
    output = ''

    for item in items:
        output += item[0] + '<br>'  # 날짜
        output += str(item[1]) + '<br>'  # 미세먼지 수치
        output += str(item[2]) + '<br>' + '<br>'  # 미세먼지 상태 정도
    return ReturnButton + thismonthseoulbutton + output


@app.route('/busan', methods=['POST'])
def show_Dust_busan():
    global sqlconnectstate
    global cursor
    global conn
    if sqlconnectstate == 0:
        activesql()

    cursor.execute('''SELECT * FROM busan order by datetime desc''')
    items = cursor.fetchall()
    output = ''

    for item in items:
        output += item[0] + '<br>'
        output += str(item[1]) + '<br>'
        output += str(item[2]) + '<br>' + '<br>'
    return ReturnButton + thismonthbusanbutton + output


@app.route('/incheon', methods=['POST'])
def show_Dust_incheon():
    global sqlconnectstate
    global cursor
    global conn
    if sqlconnectstate == 0:
        activesql()

    cursor.execute('''SELECT * FROM incheon order by datetime desc''')
    items = cursor.fetchall()
    output = ''

    for item in items:
        output += item[0] + '<br>'
        output += str(item[1]) + '<br>'
        output += str(item[2]) + '<br>' + '<br>'
    return ReturnButton + thismonthincheonbutton + output


@app.route('/dbupdate', methods=['POST'])
def UpdateDustdata():  # 미세먼지 db를 최신화 시켜줌(어제 날짜까지)
    global sqlconnectstate
    global cursor
    global conn
    if sqlconnectstate == 0:
        activesql()

    for item in dustdata:
        seoul_dust = int(item.find('seoul').text)
        busan_dust = int(item.find('busan').text)
        incheon_dust = int(item.find('incheon').text)  # api에 들어있는 지역 정보 중 인천의 해당 날짜 미세먼지 수치
        recvdate = item.find('datatime').text  # 날짜

        sql_seoul = '''INSERT IGNORE INTO seoul (datetime, dustvalue, state) VALUES(%s, %s, %s)'''
        sql_incheon = '''INSERT IGNORE INTO incheon (datetime, dustvalue, state) VALUES(%s, %s, %s)'''
        sql_busan = '''INSERT IGNORE INTO busan (datetime, dustvalue, state) VALUES(%s, %s, %s)'''

        cursor.execute(sql_seoul, (recvdate, seoul_dust, dust_state(seoul_dust)))
        cursor.execute(sql_busan, (recvdate, busan_dust, dust_state(busan_dust)))
        cursor.execute(sql_incheon, (recvdate, incheon_dust, dust_state(incheon_dust)))

    conn.commit()
    conn.close()
    sqlconnectstate = 0  # sql 접속을 끊었으므로 상태변수 바꿔줌

    return ReturnButton + '<br><br><br>정보 갱신 완료!!'


if __name__ == '__main__':
    activesql()
    app.run(debug='true')
