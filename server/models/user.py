#! /usr/bin/env python
# -*- coding: utf-8 -*-

from peewee import IntegerField, CharField
from .base import BaseModel

class User(BaseModel):
    name = CharField()

    def follow(self, user):
        from .followship import FollowShip
        return FollowShip.follow(self, user)

    def get_followers(self):
        return (f.follower for f in self.followees)

    def get_followees(self):
        return (f.followeree for f in self.followers)
