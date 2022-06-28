from flask import Blueprint,render_template,url_for
import testdb
from pybo.models import Question  #이래야 퀘스천 DB에 접근할 수 있어
from werkzeug.utils import redirect

bp = Blueprint('main',__name__,url_prefix='/')

@bp.route('/')
def index() :
    return redirect(url_for('question.questionlist')) #''안 부분을 naver.com등으로 활용   블루프린트에 해당하는 주소를 가져오는 게
    # 블루프린트   라우팅으로 되어 있는 함수의 이름을 찾아주는 것  /question/questionlist라고 쓰는 것과 같다.

    '''                                                   
    question_list = Question.query.order_by(Question.create_date.desc())
    for temp in question_list:
        print(temp.subject)
    return render_template('question/question_list.html', question_list = question_list)  #db에서 게시판처럼 질문을 보여주는 역할
                            #html안에 변수를 넣고 싶을 때 이와 같이  ~~~ = ~~~ 넣으면 됨.  전달해준 정보를 변수로. html에서 쓸수있게
   '''

@bp.route('/detail/<int:question_id>/')
def detail(question_id) :
    question = Question.query.get_or_404(question_id)  #get_or_404는 페이지 없을 때
    return render_template('question/question_detail.html',question = question)

@bp.route('/hello')
def hello_pybo() :
    return 'hello,pybo'

@bp.route('/blog')
def blog() :
    return '네이버 블로그'

@bp.route('/dbtest')
def dbtest():
    testdb.test1()
    testdb.getall_question()
    return '성공'  #이
