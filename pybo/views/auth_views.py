from flask import Blueprint,url_for,render_template,flash,request, session, g
from werkzeug.security import generate_password_hash, check_password_hash   #비밀번호를 암호화하는 작업
from werkzeug.utils import redirect

from pybo import db
from pybo.forms import UserCreateForm,UserLoginForm
from pybo.models import User

bp = Blueprint('auth',__name__,url_prefix='/auth')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)  #g.user에 있으면 로그인되어 있는 상태.  g.user는 플라스크 어디에서든 쓸 수 있음.

@bp.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('main.index'))


@bp.route('/login/', methods=('GET', 'POST'))
def login():
    form = UserLoginForm()

    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            error = '존재하지 않는 사용자입니다.'
        elif not check_password_hash(user.password, form.password.data):
            error = '비밀번호가 올바르지 않습니다.'

        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('main.index'))
        flash (error)
    return render_template('auth/login.html', form=form)



@bp.route('/signup/', methods=('GET', 'POST'))
def signup():                                        #이 주소로 불러오면 signup.html로 이동하라
    #print('============================================1')
    form = UserCreateForm()
    #print('============================================2')

    if request.method == 'POST' and form.validate_on_submit():
        #print('============================================3')
        user = User.query.filter_by(username=form.username.data).first()  #유저 이름이 중복되는 것을 막아주기 위해 한번더 넣어줌

        if not user:
            #print('============================================4')
            user = User(username=form.username.data, password=generate_password_hash(form.password1.data),email=form.email.data)
            # 모델을 만든 것임
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.index'))
        else:
            flash('이미 존재하는 사용자입니다.')

    else:
        return render_template('auth/signup.html',form=form)

