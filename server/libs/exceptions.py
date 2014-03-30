#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 WooParadog <guohaochuan@gmail.com>
#
# Distributed under terms of the MIT license.

class WhisperBaseException(Exception):
    code = 1000
    msg = "unknown error"

class HasAlreadyFolowedException(WhisperBaseException):
    code = 1001
    msg = "User Already followed"
