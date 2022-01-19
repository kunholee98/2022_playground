from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    return 'Hello, pybo! with bp'

@bp.route('/')
def index():    
    # question 내의 _list에 해당하는 URL로 리다이렉트할 수 있다.
    # question은 등록된 블루프린트 이름, _list는 블루프린트에 등록된 함수명
    # url_for 을 이용하면 하드코딩에 비해 유지 보수가 굉장히 편하다.
    return redirect(url_for('question._list'))