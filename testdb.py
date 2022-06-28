from pybo.models import Question,Answer
from datetime import datetime
from pybo import db

def test():
    q = Question(subject='질문1입니다.',content='질문1에 대한 내용입니다.', create_date=datetime.now())
    db.session.add(q)  #pybo.db에 여기 있는 내용(q)을 더해라
    db.session.commit()  #commit하는 순간 db에 저장됨 commit는 한번만

def test1() :
    for temp in range(1,11):
        s = '질문 {}'.format(temp)
        c = '질문 {}에 대한 내용입니다.'.format(temp)
        q = Question(subject=s, content=c, create_date=datetime.now())
        db.session.add(q)
        db.session.commit()
    db.session.commit()

def getall_question() :  #모든 질문을 가져오는 함수
    '''
    result = Question.query.all()  #query해서 다 가져와
    for temp in result :
        print(temp.subject)
        print(temp.content)
    '''
    result = Question.query.get(1)
    db.session.delete(result)
    db.session.commit()  #db 한줄씩 삭제하는 기능도 알아두기







