#!/usr/bin/env python2
# coding: utf-8
# file: zhulong.py
# time: 16-8-7 16:12

from flask_script import Manager, Server
from flask_migrate import MigrateCommand

from Web import web, db
from Web.models import ZhulongUser, ZhulongUserContainers
from Web.models import ZhulongSystemImages, ZhulongUserImages

__author__ = "lightless"
__email__ = "root@lightless.me"

"""
实际上这个文件相当于manage.py
控制Flask的入口以及shell环境
"""

# 设置manager
manager = Manager(web)

# 添加命令
manager.add_command("runserver", Server(host="127.0.0.1"))
manager.add_command("db", MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(
        web=web, db=db, ZhulongUser=ZhulongUser, ZhulongUserContainers=ZhulongUserContainers,
        ZhulongSystemImages=ZhulongSystemImages, ZhulongUserImages=ZhulongUserImages
    )


if __name__ == '__main__':
    manager.run()
