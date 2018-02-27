#!/usr/bin/env python
# -*- coding: utf-8 -*-   
import time
class RecAnnounce(object):
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args
    def __call__(self):
        apply(self.func, self.args)
                   