from pybo import db

# 질문 클래스
# String은 글자수 제한, Text는 글자수 제한 X
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    createdAt = db.Column(db.DateTime(), nullable=False)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    questionId = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    # backref는 역참조 가능하게 해주며, question.answer_set으로 불러올 수 있음
    # 데이터베이스 도구에서 쿼리를 이용해서 삭제하는 경우가 아닌, 파이썬 코드 a_question.delete() 와 같이 삭제하는 경우
    # cascade하게 답변이 삭제되지 않기 때문에 이를 도와줄 수 있도록 cascade 매개변수 추가
    question = db.relationship('Question', backref=db.backref('answer_set', cascade='all, delete-orphan'))
    content = db.Column(db.Text(), nullable=False)
    createdAt = db.Column(db.DateTime(), nullable=False)
