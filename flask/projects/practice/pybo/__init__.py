from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import config

# create_app 밖에서 선언하여 다른 모듈에서도 사용할 수 있다.
# 객체 초기화만 create_app 내에서 진행
db = SQLAlchemy()
migrate = Migrate()


# create_app을 application factory라 부르며 app 객체를 생성해 이를 반환하는 형식
# app을 전역으로 선언하면 프로젝트 규모가 커질수록 문제가 발생할 수 있고, 순환 참조 오류가 대표적으로 발생한다.
def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    # @ 애너테이션으로 매핑되는 함수는 라우트 함수라 부른다.
    # 새로운 URL이 필요할 때마다 create_app에 추가해주어야하는 불편함을 개선하고자 Blueprint 클래스를 이용할 수 있다.
    # @app.route('/')
    
    # blueprint 모듈을 이용하면 bp 객체를 등록만 하면 쉽게 라우트를 확장시킬 수 있다.
    from .views import main_views, question_views, answer_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)

    # filter 사용
    # flask에서 filter를 사용하고자 한다면 이를 jinja_env에 등록해줘야한다.
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime

    return app