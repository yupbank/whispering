#! /usr/bin/env python
# -*- coding: utf-8 -*-

from peewee import CharField
from .base import BaseModel, database

class User(BaseModel):
    name = CharField()

    def follow(self, user):
        from .followship import FollowShip
        return FollowShip.follow(self, user)

    def get_followers(self):
        return (f.follower for f in self.followees)

    def get_followees(self):
        return (f.followeree for f in self.followers)

    @database.commit_on_success
    def whisper(self, gossip):
        from .gossip import Gossip
        for friend in self.get_followers():
            Gossip.create(
                    content=gossip,
                    received_user=friend
                    ).save()
