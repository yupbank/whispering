#! /usr/bin/env python
# -*- coding: utf-8 -*-

from .base import BaseHandler
from .timeline import TimeLineHandler

api_handlers = []

for k, v in dict(globals()).iteritems():
    if type(v) is type and \
            issubclass(v, BaseHandler) and\
            v is not BaseHandler:
        api_handlers.append((getattr(v, 'url_path'), v))
