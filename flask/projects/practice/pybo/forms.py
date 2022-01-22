from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

# FlaskForm을 상속하여 QuestionForm을 구성
class QuestionForm(FlaskForm):
    # 첫번째 인자는 폼 라벨, validators는 검증을 위해 사용되는 도구들 (필수 항목인가, 이메일인가, 길이는 어떠한가 등)
    subject = StringField('제목', validators=[DataRequired("제목을 입력해주세요.")])
    content = TextAreaField('내용', validators=[DataRequired("내용을 입력해주세요.")])

class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired("답변을 입력해주세요.")])