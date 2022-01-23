from pybo import db

# 질문 클래스
# String은 글자수 제한, Text는 글자수 제한 X
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    # 만약 새롭게 필드를 추가할 때 nullable=False로 지정한다면, 기존에 존재하던 튜플들에서 오류가 발생할 수 있다.
    # 이를 해결하기 위해서는 일단 nullable=True로 설정하고 user_id를 임의의 값으로 설정한 후 (server_default 이용)
    # default: 새로 생성되는 값의 디폴트 / server_default: 이미 있던 튜플들에도 적용
    # migrate, upgrade 하고 False 변경 후 다시 migrate, upgrade 진행
    # 만약 upgrade 과정에서 실패했을 경우, 현재 리버전을 최종 리버전으로 옮겨야하기 때문에 flask db stamp heads 이용
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('question_set'))
    createdAt = db.Column(db.DateTime(), nullable=False)
    updatedAt = db.Column(db.DateTime(), nullable=True)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    questionId = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    # backref는 역참조 가능하게 해주며, question.answer_set으로 불러올 수 있음
    # 데이터베이스 도구에서 쿼리를 이용해서 삭제하는 경우가 아닌, 파이썬 코드 a_question.delete() 와 같이 삭제하는 경우
    # cascade하게 답변이 삭제되지 않기 때문에 이를 도와줄 수 있도록 cascade 매개변수 추가
    question = db.relationship('Question', backref=db.backref('answer_set', cascade='all, delete-orphan'))
    content = db.Column(db.Text(), nullable=False)
    user_id = db.Column('user_id', db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('answer_set'))
    createdAt = db.Column(db.DateTime(), nullable=False)
    updatedAt = db.Column(db.DateTime(), nullable=True)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
