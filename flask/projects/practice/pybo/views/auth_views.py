# 데코레이터 함수 functools
import functools
# flash는 필드 자체 오류가 아닌 프로그램 논리 오류를 발생시키는 함수
from flask import Blueprint, url_for, render_template, flash, request, session, g
# 암호화된 비밀번호 생성하는 모듈
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from pybo import db
from pybo.forms import UserCreateForm, UserLoginForm
from pybo.models import User

bp = Blueprint('auth', __name__, url_prefix="/auth")

# 라우트 함수보다 먼저 실행되는 애너테이션
# load_logged_in_user 함수는 모든 라우트 함수보다 먼저 실행되어 로그인 여부를 조사할 것이다.
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        # g는 플라스크에서 제공하는 컨텍스트 변수
        # request 변수와 마찬가지로 요청 -> 응답 과정에서 유효
        g.user = None
    else:
        g.user = User.query.get(user_id)




# GET: 계정 등록 템플릿 렌더링 / POST: 계정 등록 처리
@bp.route('/signup/', methods=('GET', 'POST'))
def signup():
    form = UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            user = User(username=form.username.data, password=generate_password_hash(form.password1.data), email=form.email.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.index'))
        else:
            flash('이미 존재하는 사용자입니다.')
    return render_template('auth/signup.html', form=form)

@bp.route('/login/', methods=('GET', 'POST'))
def login():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            error = "존재하지 않는 사용자입니다."
        elif not check_password_hash(user.password, form.password.data):
            error = "비밀번호가 올바르지 않습니다."
        if error is None:
            # session이란 플라스크 서버를 구동하는 동안에 영구히 참조할 수 있는 값.
            # 단, 시간제한이 있어서 일정 시간 접속하지 않으면 자동 삭제
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for("main.index"))
        flash(error)
    return render_template('auth/login.html', form=form)

@bp.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('main.index'))

def login_required(view):
    # @login_required 라는 애너테이션을 입력하면 자동적으로 이 데코레이터 함수가 먼저 실행된다.
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view
