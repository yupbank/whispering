#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

@pytest.mark.usefixtures("database")
class BaseTestCase(object):
    pass
