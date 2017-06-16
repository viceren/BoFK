# -*- coding: utf-8 -*-
# @Author: viceren
# @Date:   2017-06-05 13:50:45
# @Last Modified by:   viceren
# @Last Modified time: 2017-06-05 15:17:00
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)
