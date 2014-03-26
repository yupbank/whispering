#! /usr/bin/env python
# -*- coding: utf-8 -*-


from peewee import IntegerField, CharField, ForeignKeyField, TextField
from .base import make_base_model
from .user import User

class Gossip(make_base_model()):
    to_friends = ForeignKeyField(User, related_name="received_gossips")
    content = TextField()
