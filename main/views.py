#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: viceren
# @Date:   2017-06-16 14:24:46
# @Last Modified by:   viceren
# @Last Modified time: 2017-06-16 16:33:05


import os
from flask import Flask


@main.route('/', methods=['GET', 'POST'])
def index():
    form = PostForm()
    if current_user.can(Permission.WRITE_ARTICLES) and \
            form.validate_on_submit():
        post = Post(body=form.body.data,
                    author=current_user._get_current_object())
        db.session.add(post)
        return redirect(url_for('.index'))
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('index.html', form=form, posts=posts)
