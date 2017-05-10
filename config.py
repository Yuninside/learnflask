import os

basedir = os.path.abspath(os.path.dirname(__file__))

# 通用配置
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = '13610233769@163.com'    # 邮件用户名
    MAIL_PASSWORD = '19930924hzy'             # 邮件密码
    FLASK_MAIL_SUBJECT_PREFIX = '[Yuninside]'  # 主题
    FLASK_MAIL_SENDER = '13610233769@163.com'   # 发件人
    FLASK_ADMIN = '779032597@qq.com'            # 收件人
    
    
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    
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