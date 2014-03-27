#! /usr/bin/env python
# -*- coding: utf-8 -*-

from config import DATABASE_BACKEND, DATABASE_CONNECTION_PARAMS
from peewee import MySQLDatabase, Model, SqliteDatabase

DATABASE_BACKENDS = {
        'sqlite3': SqliteDatabase,
        'mysql': MySQLDatabase
        }

backend = DATABASE_BACKENDS.get(DATABASE_BACKEND)

if not backend:
    raise KeyError("No Schema")

database = backend(**DATABASE_CONNECTION_PARAMS)

class BaseModel(Model):
    class Meta(object):
        database = database
