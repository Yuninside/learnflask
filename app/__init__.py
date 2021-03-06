from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment 
from flask_sqlalchemy import SQLAlchemy 
from config import config

from flask_mail import Mail 

from flask_login import LoginManager   #用户登陆

mail = Mail()  #  邮件

bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()

# 用户登陆
login_manager = LoginManager()
login_manager.session_protection = 'strong'  #属性可设置为None basic strong 提供不同安全等级
login_manager.login_view = 'auth.login'




def  create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    
    login_manager.init_app(app)   # 登陆账户


    # 注册蓝本  
    # 添加路由和自定义的错误页面
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_perfix = '/auth')


    return app

