#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: viceren
# @Date:   2017-05-17 15:25:03
# @Last Modified by:   viceren
# @Last Modified time: 2017-05-24 10:32:05

from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import abort
from flask_script import Manager


app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def index():
    response = make_response("<h1> This document carries a cookie</h1>")
    response.set_cookie("answer", "42")
    return render_template('index.html')


@app.route('/redirect')
def redirect_web():
    return redirect("http://localhost:5000")


@app.route('/user/<name>')
def get_user(name):
    user = load_user(name)
    if not user:
        abort(404)
    return render_template('get_user', user.name=name)


@app.route('/ua')
def ua():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent, 400


if __name__ == '__main__':
    manager.run()
