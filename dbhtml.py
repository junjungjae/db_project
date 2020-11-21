from flask import Flask
import pymysql

app = Flask(__name__)
conn = pymysql.connect(host='localhost', user='root', password='smile1996', db='dbprac', charset='utf8')
cursor = conn.cursor()

@app.route('/')
def mainpage():
    return "Seoul, Incheon, Busan Dust Information"


@app.route('/seoul')
def show_Dust_seoul():
    cursor.execute('''SELECT * FROM seoul''')
    items = cursor.fetchall()
    print("seoul's dust Information")

    output = ''
    for item in items:
        output += item[0] + '<br>'
        output += str(item[1]) + '<br>'
        output += str(item[2]) + '<br>' + '<br>'
    return output


@app.route('/busan')
def show_Dust_busan():
    cursor.execute('''SELECT * FROM busan''')
    items = cursor.fetchall()
    print("busan's dust Information")

    output = ''
    for item in items:
        output += item[0] + '<br>'
        output += str(item[1]) + '<br>'
        output += str(item[2]) + '<br>' + '<br>'
    return output


@app.route('/incheon')
def show_Dust_incheon():
    cursor.execute('''SELECT * FROM incheon''')
    items = cursor.fetchall()
    print("incheon's dust Information")

    output = ''
    for item in items:
        output += item[0] + '<br>'
        output += str(item[1]) + '<br>'
        output += str(item[2]) + '<br>' + '<br>'
    return output

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)