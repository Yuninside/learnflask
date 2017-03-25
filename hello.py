
from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap

from flask_wtf import FlaskForm     # 导入扩展模块
from wtforms import StringField, SubmitField
from wtforms.validators import Required      # 验证函数，确保字段不为空

from flask import session, redirect, url_for, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

'''
@app.route('/')
def index():
    response = make_response('<h1> this document carries a cookie! </h1>')
    response.set_cookie('answer', '42')
    return response
'''

bootstrap = Bootstrap(app)


'''
@app.route('/')
def index():
    return render_template('index.html')

'''


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators = [Required()])     # 用户可以输入内容的文本框，值被name变量接收
    submit = SubmitField('Submit')     # 提交按钮

@app.route('/', methods = ['GET', 'POST'])     #告诉Flask做URL映射中把这个视图函数注册为GET和POST请求的处理程序
def index():
    form = NameForm()
    if form.validate_on_submit():     #如果输入的数据验证通过，validate_on_submit()方法返回True
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('look like you have changed your name!')
        session['name'] = form.name.data     #赋值给局部变量
        return redirect(url_for('index'))          
    return render_template('index.html', form=form, name=session.get('name'))

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name = name)



if __name__ == '__main__':
    app.run(debug =True)

