#! /usr/bin/env python
# -*- coding: utf-8 -*-


from peewee import ForeignKeyField, TextField
from .base import BaseModel
from .user import User

class Gossip(BaseModel):
    received_user = ForeignKeyField(User, related_name="received_gossips")
    content = TextField()
