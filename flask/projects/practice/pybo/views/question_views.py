from flask import Blueprint, render_template

from pybo.models import Question

bp = Blueprint('question', __name__, url_prefix="/question")

@bp.route('/list/')
def _list():
    # Question 모델에서 createdAt의 내림차순으로 정렬하여 쿼리를 불러온다.
    question_list = Question.query.order_by(Question.createdAt.desc())
    # render_template: 템플릿 파일을 화면으로 렌더링하는 함수 (여기서 템플릿 파일은 question/question_list.html 이다.)
    return render_template('question/question_list.html', question_list=question_list)

@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    # get_or_404 : HTTP request code가 404인 경우 오류 페이지 출력
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question)