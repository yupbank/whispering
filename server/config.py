#! /usr/bin/env python
# -*- coding: utf-8 -*-

DEBUG = False
DATABASE_BACKEND = "mysql"
DATABASE_CONNECTION_PARAMS = {}

try:
    from local_config import *
except:
    pass
