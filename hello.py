import os
from flask import Flask
from flask import render_template      
from flask_bootstrap import Bootstrap   # 导#入bootstrap 前端框架

from flask_script import Manager   # manager命令行模式
from flask_moment import Moment   #

from flask_wtf import FlaskForm     # 导入扩展模块
from wtforms import StringField, SubmitField
from wtforms.validators import Required      # 验证函数，确保字段不为空

from flask import session, redirect, url_for, flash    # 

from flask_sqlalchemy import SQLAlchemy      # sqlalchemy数据库框架

from flask_migrate import Migrate, MigrateCommand  # 数据库迁移框架


# 数据库在本机的路径
basedir = os.path.abspath(os.path.dirname(__file__))



app = Flask(__name__)

app.config['SECRET_KEY'] = 'hard to guess string'

# 配置一个SQLite数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWM'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# 初始化数据库 
db = SQLAlchemy(app)

# 初始化前端框架
bootstrap = Bootstrap(app)

# 初始化manager模式
manager = Manager(app)

# 定义时间
moment = Moment(app)


migrate = Migrate(app, db)
manager.add_command('db',MigrateCommand)



#定义Role 和 User 模型
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique = True)
    users = db.relationship('User', backref = 'role', lazy = 'dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique = True, index = True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username



# 表单类
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators = [Required()])     # 用户可以输入内容的文本框，值被name变量接收
    submit = SubmitField('Submit')     # 提交按钮




#定义页面
@app.route('/', methods = ['GET', 'POST'])     #告诉Flask做URL映射中把这个视图函数注册为GET和POST请求的处理程序
def index():
    form = NameForm()
    if form.validate_on_submit():     #如果输入的数据验证通过，validate_on_submit()方法返回True
        user = User.query.filter_by(username = form.name.data).first()
        if user is None:
            user = User(username = form.name.data)
            db.session.add(user)
            session['known'] = False 
        else:
            session['known'] = True
        session['name'] = form.name.data     #赋值给局部变量
        form.name.data = ''
        return redirect(url_for('index'))     
    return render_template('index.html', 
        form=form, name=session.get('name'),
        known = session.get('known', False))


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name = name)



if __name__ == '__main__':
    # 调试模式
 #   app.run(debug =True)

    #命令行模式
    manager.run()

    
