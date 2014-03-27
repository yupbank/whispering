#! /usr/bin/env python
# -*- coding: utf-8 -*-

from peewee import ForeignKeyField, IntegrityError
from .base import BaseModel, database
from .user import User
from libs.exceptions import HasAlreadyFolowedException

class FollowShip(BaseModel):
    follower = ForeignKeyField(User, related_name="followers")
    followeree = ForeignKeyField(User, related_name="followees")

    class Meta:
        indexes = (
                (('follower', 'followeree'), True),
                (('followeree', 'follower'), True),
                )

    @classmethod
    @database.commit_on_success
    def follow(cls, follower, followeree):
        try:
            cls.create(follower=follower, followeree=followeree)
        except IntegrityError:
            raise HasAlreadyFolowedException
