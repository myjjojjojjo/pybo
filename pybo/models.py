from pybo import db
#퀘스천 테이블의 구조생성 (id와 subject등은 칼럼)
class Question(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)  #string대신 text도 가능. text는 제한이 없어 문제가 되기도.
    content = db.Column(db.Text(),nullable=False)        # nullable는 제목은 꼭 있어야 한다는 뜻
    create_date = db.Column(db.DateTime(),nullable=False)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150),unique=True,nullable=False)  # unique는 중복을 허락하지 않는다는 의미.
    password = db.Column(db.String(200),nullable=False)
    email = db.Column(db.String(120),unique=True, nullable=False)