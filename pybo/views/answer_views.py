from flask import Blueprint,render_template,url_for,request  #답변등록 누르는순간 답변등록 안 정보를 뽑아오기위해 request
import testdb
from pybo import db  #pybo폴더라 그런듯
from pybo.models import Question,Answer
from werkzeug.utils import redirect
from datetime import datetime
from ..forms import  AnswerForm


bp = Blueprint('answer',__name__,url_prefix='/answer')

@bp.route('/create/<int:question_id>',methods=('POST',))  #'/create/<int:question_id>'는 get이라는 method를 쓸 때.
def create(question_id):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)

    if form.validate_on_submit():

        answer = Answer(content=form.content.data, create_date=datetime.now())  #models의 Answer임
        question.answer_set.append(answer)  #answer_set은 답변모음.  저장하는 이유는 질문삭제시 답변도 같이 삭제되도록 관리하기 위해. 또한
        db.session.commit()                 #db.session.add(answer) 해도 된다.
        return redirect(url_for('question.detail',question_id=question_id))

    return render_template('question/question_detail.html',question=question, form=form)




