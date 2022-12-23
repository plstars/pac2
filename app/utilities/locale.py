#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PRD / DEV environment definitions
import os

from dotenv import load_dotenv

load_dotenv("./.env")


def get_env_variable(name):
    """Sets GLOBAL constants from the shell enviroment

    Args:
        name (text): Environment variable name

    Raises:
        Exception: In the event the environment variable is not set in the shall

    Returns:
        text: value of the environment variable
    """
    try:
        # print (name, os.environ[name])
        return os.environ[name]
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)


CS_GITROOT = get_env_variable("CS_GITROOT")

# GLOBAL CONSTANTS
PAYMENT_REQUEST = "!! Pmt Req !!"
