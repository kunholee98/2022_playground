from datetime import datetime

from flask import Blueprint, url_for, request, render_template, g
from werkzeug.utils import redirect

from .. import db
from ..forms import AnswerForm
from ..models import Question, Answer
from pybo.views.auth_views import login_required

bp = Blueprint('answer', __name__, url_prefix="/answer")

@bp.route("/create/<int:question_id>", methods=('POST',))
@login_required
def create(question_id):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    if form.validate_on_submit():
        content = request.form['content']
        answer = Answer(content=content, createdAt=datetime.now(), user=g.user)
        question.answer_set.append(answer)
        db.session.commit()
        return redirect(url_for('question.detail', question_id=question_id))
    return render_template('question/question_detail.html', question=question, form=form)
    
    # question = Question.query.get_or_404(question_id)
    # # request에 form에 담긴 정보들이 담겨있다. (브라우저에서 요청한 객체가 담겨있다.)
    # content = request.form['content']
    # answer = Answer(content=content, createdAt=datetime.now())
    # question.answer_set.append(answer)
    # db.session.commit()
    # return redirect(url_for('question.detail', question_id=question.id))