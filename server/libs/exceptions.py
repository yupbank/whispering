#! /usr/bin/env python
# -*- coding: utf-8 -*-

class WhisperBaseException(Exception):
    err_no = 0
    msg = ""

class HasAlreadyFolowedException(WhisperBaseException):
    err_no = 1001
    msg = "已经关注过"
