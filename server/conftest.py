#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pytest
import config

test_db = "tests/test.db"
config.DATABASE_BACKEND = "sqlite3"
config.DATABASE_CONNECTION_PARAMS = {
        'database': test_db
        }

def load_databases():
    try:
        os.unlink(test_db)
    except OSError:
        pass
    from models.user import User
    from models.followship import FollowShip
    from models.gossip import Gossip
    User.create_table()
    FollowShip.create_table()
    Gossip.create_table()

load_databases()

def create_test_user(name):
    from models.user import User
    user1 = User.create(name=name)
    user1.save()
    return user1

@pytest.fixture(scope="session")
def user1():
    return create_test_user('test1')

@pytest.fixture(scope="session")
def user2():
    return create_test_user('test1')
