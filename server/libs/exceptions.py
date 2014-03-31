#! /usr/bin/env python
# -*- coding: utf-8 -*-

class WhisperBaseException(Exception):
    code = 1000
    msg = "unknown error"

class HasAlreadyFolowedException(WhisperBaseException):
    code = 1001
    msg = "User Already followed"
