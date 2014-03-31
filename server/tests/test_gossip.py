#! /usr/bin/env python
# -*- coding: utf-8 -*-

from framework import BaseTestCase

class TestGossip(BaseTestCase):
    def test_send_gossip(self, user1, user2):
        user1.follow(user2)
        user2.whisper("test")
        list(user1.received_gossips)
