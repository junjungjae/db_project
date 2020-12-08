# db_project

프로그램 설명 : html 페이지 접속 시 [서울 미세먼지] [부산 미세먼지] [인천 미세먼지] [정보 갱신] 총 4개의 버튼이 있습니다

서울, 부산 인천 미세먼지 버튼은 과거 기간동안의 하루 평균 미세먼지 수치와 그에 따른 상태를 표시해줍니다.
정보 갱신 버튼은 공공데이터 api로부터 최신화된 정보를 받아와 db에 저장하게 됩니다.
각 페이지 진입 시 상단의 [홈으로] 버튼을 통해 다시 메인 페이지로 돌아갈 수 있습니다

실행 방법
1. template 폴더와 app.py 파일을 동일한 파이썬 프로젝트 폴더에 넣습니다.
2. app.py를 실행시킵니다
3. 콘솔 창에 뜬 http://127.0.0.1:5000 주소에 접속합니다.

-----------------------------------------------------------------
hello.html과 recvopenapi.py는 프로젝트 진행 과정에서 학습한 내용에 대해 정리해 놓은 파일이며
실행에는 template 폴더와 app.py만 있으면 됩니다.
