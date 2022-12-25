#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 18:19:21 2019

@author: tim
"""

from app.utilities import locale as pll


def get_environment() -> None:
    return pll.CS_GITROOT


def show_testing() -> None:
    return "TEST_DATA"


# End
