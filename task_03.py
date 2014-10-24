#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Lesson 08, Task 03 file"""


import time


class Snapshot(object):
    """The time something happened.

    Args:
        created(date/time): timestamp when something was created

    Attributes:
        created(timestamp): when something was made
    """

    def __init__(self):
        self.created = time.time()