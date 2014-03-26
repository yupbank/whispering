#! /usr/bin/env python
# -*- coding: utf-8 -*-

from .base import BaseHandler

class TimeLineHandler(BaseHandler):
    url_path = "/"

    def get(self):
        self.finish("ok")
