from flask import Flask
from flask_mail import Mail, Message


from flask_script import Manager, Shell # manager命令行模式



app = Flask(__name__)


mail = Mail(app)

manager=Manager(app)

app.config.update(
    MAIL_SERVER='smtp.163.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='13610233769@163.com',
    MAIL_PASSWORD='19930924yy'
)


'''

@app.route('/')
def index():
    msg = Message(subject="mongo", sender='13610233769@163.com', recipients=['779032597@qq.com'])
    msg.html='<h1>hello word</h1>'
    mail.send(msg)
    return "FUCK THE WORLD"

'''

if __name__ == '__main__':
    manager.run()