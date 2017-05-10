#!/usr/bin/env python
import os
from app import create_app, db
from app.models import User, Role
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand


app = create_app('default')   #默认配置
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():          # shell会话
    return dict(app=app, db=db, User=User, Role=Role)
manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command 
def test():
    """Run the unit test"""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    
    #命令行模式启动，启动命令： manager.py runserver
    manager.run()

    
