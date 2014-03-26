#! /usr/bin/env python
# -*- coding: utf-8 -*-

from peewee import IntegerField, CharField, ForeignKeyField
from .base import make_base_model
from .user import User

class Contact(make_base_model()):
    from_id = ForeignKeyField()
    to_id = ForeignKeyField()

    @classmethod
    def follow(cls, from_user, to_user):
        contact = cls.create(from_id=from_user.id, to_id=to_user.id)
        contact.save()
        return contact
