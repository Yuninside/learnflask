from flask import Blueprint

main = Blueprint('main', __name__)   # 创建蓝本，第一个参数是蓝本名字，第二个参数是蓝本所在的模块。

from . import views, errors 