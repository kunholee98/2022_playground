from flask import Flask

# create_app을 application factory라 부르며 app 객체를 생성해 이를 반환하는 형식
# app을 전역으로 선언하면 프로젝트 규모가 커질수록 문제가 발생할 수 있고, 순환 참조 오류가 대표적으로 발생한다.
def create_app():
    app = Flask(__name__)

    # @ 애너테이션으로 매핑되는 함수는 라우트 함수라 부른다.
    # 새로운 URL이 필요할 때마다 create_app에 추가해주어야하는 불편함을 개선하고자 Blueprint 클래스를 이용할 수 있다.
    # @app.route('/')
    
    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app