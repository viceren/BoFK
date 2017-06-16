#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: viceren
# @Date:   2017-06-07 10:13:38
# @Last Modified by:   viceren
# @Last Modified time: 2017-06-07 10:22:16

import unittest
from flask import current_app
from app import current_app, db


class BasicsTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])
