#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pytest
from peewee import SqliteDatabase

TEST_DB_PATH = 'tests/test.db'

@pytest.yield_fixture
def database(monkeypatch):
    database = SqliteDatabase(TEST_DB_PATH)
    database.connect()
    monkeypatch.setattr("models.base.BaseModel._meta.database", database)
    from models.user import User
    from models.followship import FollowShip
    User.create_table()
    FollowShip.create_table()
    yield
    database.close()
    os.unlink(TEST_DB_PATH)

def create_test_user(name):
    from models.user import User
    user1 = User.create(name=name)
    user1.save()
    return user1

@pytest.fixture
def user1():
    return create_test_user('test1')

@pytest.fixture
def user2():
    return create_test_user('test1')
