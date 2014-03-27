#! /usr/bin/env python
# -*- coding: utf-8 -*-

from peewee import MySQLDatabase, Model

database = MySQLDatabase('localhost', '')

class BaseModel(Model):
    class Meta(object):
        database = database
