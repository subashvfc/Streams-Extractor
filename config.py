#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


import os

class Config(object):

    # Get a bot token from botfather
    BOT_TOKEN = os.environ.get("5404778856:AAG4IObcdt7PIR7MQLuRZ74vnb9vGT4vFjk", "")


    # Get from my.telegram.org (or @UseTGXBot)
    APP_ID = int(os.environ.get("17545386", ""))
    API_HASH = os.environ.get("f1d5ee6adccd34db0aab30115f4c30db", "")


    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("989262779", "").split())
    
