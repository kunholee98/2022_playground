from crypt import methods
from datetime import datetime
from flask import request, g, flash, render_template, redirect, url_for, Blueprint

from pybo import db
from pybo.forms import CommentForm
from pybo.views.auth_views import login_required
from pybo.models import Question, Comment, Answer

bp = Blueprint('comment', __name__, url_prefix='/comment')

@bp.route('/create/question/<int:question_id>', methods=('GET', 'POST'))
@login_required
def create_question(question_id):
    form = CommentForm()
    question = Question.query.get_or_404(question_id)
    if request.method == 'POST' and form.validate_on_submit():
        comment = Comment(user=g.user, content=form.content.data, createdAt=datetime.now(), question=question)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('question.detail', question_id=question_id))
    return render_template('comment/comment_form.html', form=form)

@bp.route('/modify/question/<int:comment_id>')
@login_required
def modify_question(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    if g.user != comment.user:
        flash("수정 권한이 없습니다.")
        return redirect(url_for('question.detail', question_id=comment.question.id))
    if request.method == 'POST':
        form = CommentForm()
        if form.validate_on_submit():
            form.populate_obj(comment)
            comment.updatedAt = datetime.now()
            db.session.commit()
            return redirect(url_for('question.detail', question_id=comment.question.id))
    else:
        form = CommentForm(obj=comment)
    return render_template('comment/comment_form.html', form=form)

@bp.route('/delete/question/<int:comment_id>')
@login_required
def delete_question(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    question_id = comment.question.id
    if g.user != comment.user:
        flash("삭제 권한이 없습니다.")
        return redirect(url_for('question.detail', question_id=question_id))
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for('question.detail', question_id=question_id))

@bp.route('/create/answer/<int:answer_id>', methods=('GET', 'POST'))
@login_required
def create_answer(answer_id):
    answer = Answer.query.get_or_404(answer_id)
    form = CommentForm()
    if request.method == 'POST' and form.validate_on_submit():
        comment = Comment(user=g.user, content=form.content.data, answer=answer, createdAt=datetime.now())
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('question.detail', question_id=answer.question.id))
    return render_template('comment/comment_form.html', form=form)

@bp.route('/modify/answer/<int:comment_id>', methods=('GET', 'POST'))
@login_required
def modify_answer(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    if g.user != comment.user:
        flash("수정 권한이 없습니다.")
        return redirect(url_for('question.detail', question_id=comment.answer.question.id))
    if request.method == 'POST':
        form = CommentForm()
        if form.validate_on_submit():
            form.populate_obj(comment)
            comment.updatedAt = datetime.now()
            db.session.commit()
            return redirect(url_for('question.detail', question_id=comment.answer.question.id))
    else:
        form = CommentForm(obj=comment)
    return render_template('comment/comment_form.html', form=form)

@bp.route('/delete/answer/<int:comment_id>')
@login_required
def delete_answer(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    question_id = comment.answer.question.id
    if g.user != comment.user:
        flash("삭제 권한이 없습니다.")
        return redirect(url_for('question.detail', question_id=question_id))
    db.session.delete(comment)
    db.session.commit()
    # comment가 삭제되기 때문에 아래와 같이 comment의 요소들을 활용하는 것은 불가능.
    # 따라서 미리 question_id를 저장해놓아야함.
    # return redirect(url_for('question.detail', question_id=comment.answer.question.id))
    return redirect(url_for('question.detail', question_id=question_id))
