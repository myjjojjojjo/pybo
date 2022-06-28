from flask import Blueprint,render_template, request, url_for
from werkzeug.utils import redirect
from ..import db                           #..은 제일 상위라는 뜻인가?
import testdb
from pybo.models import Question
from pybo.forms import QuestionForm,AnswerForm
from datetime import datetime

bp = Blueprint('question',__name__,url_prefix='/question')



@bp.route('/list/')
def questionlist() :
    page = request.args.get('page',type=int,default=1)
    question_list = Question.query.order_by(Question.create_date.desc())
    question_list = question_list.paginate(page,per_page=10) #페이지마다 글을 10개씩 보여줘라
    return render_template('question/question_list.html', question_list=question_list)

@bp.route('/detail/<int:question_id>/')
def detail(question_id) :
    form= AnswerForm()
    question = Question.query.get_or_404(question_id)  #get_or_404는 페이지 없을 때
    return render_template('question/question_detail.html',question = question,form=form)

@bp.route('/create/',methods=('GET','POST'))  #post만 쓰면 get 상황에서 불러오지 못함.
def create() :
    form = QuestionForm()

    if request.method == 'POST' and form.validate_on_submit() :  #form에 데이터가 잘 들어가있으면
        question = Question(subject=form.subject.data,content=form.content.data, create_date=datetime.now())
        db.session.add(question)  #데이터베이스에 집어넣을 준비해줘
        db.session.commit()
        return redirect (url_for('main.index'))

    return render_template('question/question_form.html',form=form) # host가 아니고 get으로 불러올 때. html불러올 때 render_template

