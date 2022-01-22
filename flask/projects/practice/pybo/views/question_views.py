from datetime import datetime

from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect

from .. import db
from pybo.models import Question
from ..forms import AnswerForm, QuestionForm


bp = Blueprint('question', __name__, url_prefix="/question")

@bp.route('/list/')
def _list():
    # pagination을 위해 페이지 값을 얻어온다.
    # localhost:5000/question/list/?page=5 으로 GET 방식으로 받아올 때 page를 저장.
    page = request.args.get('page', type=int, default=1)
    # Question 모델에서 createdAt의 내림차순으로 정렬하여 쿼리를 불러온다.
    question_list = Question.query.order_by(Question.createdAt.desc())
    question_list = question_list.paginate(page, per_page=10)
    # render_template: 템플릿 파일을 화면으로 렌더링하는 함수 (여기서 템플릿 파일은 question/question_list.html 이다.)
    return render_template('question/question_list.html', question_list=question_list)

@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    form = AnswerForm()
    # get_or_404 : HTTP request code가 404인 경우 오류 페이지 출력
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question, form=form)

@bp.route('/create', methods=('GET','POST'))
def create():
    form = QuestionForm()
    # create함수로 요청된 방식이 POST이고 전송된 폼 데이터의 정합성을 점검!
    if request.method == 'POST' and form.validate_on_submit():
        question = Question(subject=form.subject.data, content=form.content.data, createdAt=datetime.now())
        db.session.add(question)
        db.session.commit()
        # POST 이후에는 main의 index 함수로 되돌아간다.
        return redirect(url_for('main.index'))
    # GET 또는 invalid form 일 경우에는 question_form을 다시 실행. form에는 QuestionForm을 담아서 보냄.
    return render_template('question/question_form.html', form=form)