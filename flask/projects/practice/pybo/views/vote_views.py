from flask import url_for, g, flash, Blueprint
from werkzeug.utils import redirect

from pybo import db
from pybo.views.auth_views import login_required
from pybo.models import Question

bp = Blueprint('vote', __name__, url_prefix="/vote")

@bp.route('/question/<int:question_id>')
@login_required
def question(question_id):
    _question = Question.query.get_or_404(question_id)
    if g.user == _question.user:
        flash("본인의 글은 추천할 수 없습니다.")
        return redirect(url_for('question.detail', question_id=question_id))
    if g.user not in _question.voter:
        _question.voter.append(g.user)  
    else:
        _question.voter.remove(g.user)
    db.session.commit()
    return redirect(url_for('question.detail', question_id=question_id))