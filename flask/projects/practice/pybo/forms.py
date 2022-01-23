from typing import Text
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

# FlaskForm을 상속하여 QuestionForm을 구성
class QuestionForm(FlaskForm):
    # 첫번째 인자는 폼 라벨, validators는 검증을 위해 사용되는 도구들 (필수 항목인가, 이메일인가, 길이는 어떠한가 등)
    subject = StringField('제목', validators=[DataRequired("제목을 입력해주세요.")])
    content = TextAreaField('내용', validators=[DataRequired("내용을 입력해주세요.")])

class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired("답변을 입력해주세요.")])

# 유저 생성 폼
class UserCreateForm(FlaskForm):
    username = StringField('유저이름', validators=[DataRequired("유저이름을 입력해주세요."), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[DataRequired("비밀번호를 입력해주세요"), EqualTo('password2', '비밀번호가 일치하지 않습니다.')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired("다시 한번 비밀번호를 입력해주세요.")])
    # Email() 검증 시 email_validator 를 pip 해야한다.
    email = EmailField('이메일',validators=[DataRequired("이메일을 입력해주세요."), Email()])

# 유저 로그인 폼
class UserLoginForm(FlaskForm):
    username = StringField('유저이름', validators=[DataRequired("유저이름을 입력해주세요."), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired("비밀번호를 입력해주세요.")])

# 댓글 생성 폼
class CommentForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired("댓글을 입력해주세요.")])