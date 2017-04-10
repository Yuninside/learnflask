import os

basedir = os.path.abspath(os.path.dirname(__file__))

# 通用配置
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_MAIL_SUBJECT_PREFIX = '[Yuninside]'  # 主题
    FLASK_MAIL_SENDER = '13610233769@163.com'
    FLASK_ADMIN = os.environ.get('FLASK_ADMIN')
    
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'stmp.163.com'
    MAIL_PORT = 465
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or '13610233769@163.com'    # 邮件用户名
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or '19930924yy'   # 邮件密码

    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')



class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                'sqlite:///' + os.path.join(basedir, 'data.sqlite')



config = {
    'developmentconfig': DevelopmentConfig,
    'testing': TestingConfig,
    'producttionconfig': ProductionConfig,

    'default': DevelopmentConfig
}


                

