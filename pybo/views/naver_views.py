from flask import Blueprint
import pybo.naverapi as nv
from flask import request

bp = Blueprint('naver',__name__,url_prefix='/naver')

@bp.route('/blog')
def blog():
    key =  request.args.get('keyword')
    #print(key)
    result = nv.naver_blog(key)
    #네이버 api를 활용해서 블로그의 내용을 전달해주는 기능
    return {'result': result} #클라이언트에게 다시 줌