from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import MetaData

import config

naming_convention = {   # SQLite db 에서는 사용하는 인덱스 등의 제약 조건 이름을 MetaData 클래스를 사용하여 규칙 정의가 필요
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

# create_app 밖에서 선언하여 다른 모듈에서도 사용할 수 있다.
# 객체 초기화만 create_app 내에서 진행
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()


# create_app을 application factory라 부르며 app 객체를 생성해 이를 반환하는 형식
# app을 전역으로 선언하면 프로젝트 규모가 커질수록 문제가 발생할 수 있고, 순환 참조 오류가 대표적으로 발생한다.
def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):  # sqlite db를 사용할 때 오류 방지
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)
    from . import models

    # @ 애너테이션으로 매핑되는 함수는 라우트 함수라 부른다.
    # 새로운 URL이 필요할 때마다 create_app에 추가해주어야하는 불편함을 개선하고자 Blueprint 클래스를 이용할 수 있다.
    # @app.route('/')
    
    # blueprint 모듈을 이용하면 bp 객체를 등록만 하면 쉽게 라우트를 확장시킬 수 있다.
    from .views import main_views, question_views, answer_views, auth_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views.bp)

    # filter 사용
    # flask에서 filter를 사용하고자 한다면 이를 jinja_env에 등록해줘야한다.
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime

    return app