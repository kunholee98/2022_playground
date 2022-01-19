from datetime import datetime

from flask import Blueprint, url_for, request
from werkzeug.utils import redirect

from pybo import db
from pybo.models import Question, Answer

bp = Blueprint('answer', __name__, url_prefix="/answer")

@bp.route("/create/<int:question_id>", methods=('POST',))
def create(question_id):
    question = Question.query.get_or_404(question_id)
    # request에 form에 담긴 정보들이 담겨있다. (브라우저에서 요청한 객체가 담겨있다.)
    content = request.form['content']
    answer = Answer(content=content, createdAt=datetime.now())
    question.answer_set.append(answer)
    db.session.commit()
    return redirect(url_for('question.detail', question_id=question.id))