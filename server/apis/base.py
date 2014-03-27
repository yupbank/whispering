#! /usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    @property
    def url_path(self):
        raise NotImplementedError
