import os

BASE_DIR = os.path.dirname(__file__)

# 플라스크 연습이기 때문에 config.py도 함께 github에 올립니다! 오해 없으시길
# 데이터베이스 접속 주소
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
# SQLAlchemy의 이벤트를 처리하는 옵션
SQLALCHEMY_TRACK_MODIFICATIONS = False
# CSRF 토큰 / CSRF는 사용자의 요청을 위조하는 웹사이트 공격 기법으로 이 토큰을 이용하여 폼으로 전송된 데이터가 실제로 웹페이지에서 작성된 데이터인지 판단해주는 가늠자 역할을 한다.
# 즉, CSRF 토큰은 CSRF를 방어하려고 플라스크에서 생성하는 무작위 문자열을 의미한다. 여기서는 연습이기때문에 간단한 문자열을 채택했다.
# 서비스 운영 시 SECRET_KEY를 설정하는 방법은 후에 알아본다.
SECRET_KEY = "dev"