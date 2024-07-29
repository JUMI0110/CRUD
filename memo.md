서버열고 templates 폴더 생성 후 페이지 실행 시 에러 
-> 서버 닫았다가 다시 실행


ORM O = python R =SQL M = mapping
파이썬 코드를 sql언어로 번역 
번역본
makemigrations 파이썬 코드를 sql 언어로 만들기 전단계 
```bash
python manage.py makemigrations
```
모델 설계시 컬럼명 수정하면 위험 설계할 때 잘 지정

db에 반영
python manage.py migrate
sql에 적용(표 작성)

superuser 생성  admin 페이지에서 사용할 id, password 생성
python manage.py createsuperuser
문제있으면 다시 생성 가능

django - admin (관리자페이지)
데이터가 어떻게 저장되었는지 확인


crud 중 read 구성
read 데이터베이스에 있는 정보 읽기
전체게시물 전체내용 가져오는 코드 Post.objects.all()
하나의 게시물 상세내용 페이지 detail 

rdbms id -> 숫자로 이루어진 고유값
숫자 id 이용하여 url 이동 

Update 기존 정보 + 수정
update 에러 -> form의 action 값 설정하지 않으면 update(수정)해도 반영되지않음


항상 주의 '/' 빼먹으면 웹페이지가 제대로 작동하지 않을 수 있음