#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from framework import BaseTestCase

class TestUserCase(BaseTestCase):
    def test_follow_user(self, user1, user2):
        user1.follow(user2)
        assert user1 in user2.get_followers()
        assert user2 in user1.get_followees()

    def test_send_gossip(self, user1, user2):
        user1.follow(user2)
