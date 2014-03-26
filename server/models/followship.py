#! /usr/bin/env python
# -*- coding: utf-8 -*-

from peewee import IntegerField, CharField, ForeignKeyField
from .base import BaseModel
from .user import User

class FollowShip(BaseModel):
    follower = ForeignKeyField(User, related_name="followers")
    followeree = ForeignKeyField(User, related_name="followees")

    @classmethod
    def follow(cls, follower, followeree):
        contact = cls.create(follower=follower, followeree=followeree)
        contact.save()
        return contact
