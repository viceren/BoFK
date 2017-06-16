#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: viceren
# @Date:   2017-05-17 15:25:03
# @Last Modified by:   viceren
# @Last Modified time: 2017-06-05 16:12:56

from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import abort
from flask_script import Manager
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_script import Shell

app = Flask(__name__)
manager = Manager(app)
moment = Moment(app)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/redirect')
def redirect_web():
    return redirect("http://localhost:5000")


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.route('/ua')
def ua():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent, 400

if __name__ == '__main__':
    manager.run()
