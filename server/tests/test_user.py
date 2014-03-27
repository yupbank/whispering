#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from framework import BaseTestCase
from libs.exceptions import HasAlreadyFolowedException

class TestUserCase(BaseTestCase):
    def test_follow_user(self, user1, user2):
        try:
            user1.follow(user2)
        except:
            pass
        assert user1 in user2.get_followers()
        assert user2 in user1.get_followees()

        with pytest.raises(HasAlreadyFolowedException):
            user1.follow(user2)
