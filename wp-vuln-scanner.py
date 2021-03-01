#!/usr/bin/env/python

import os
import sys
import time
import datetime
import getopt
import urlparse
from core.lib import wp_colors
from core.lib import wp_print
from core.lib import wp_info
from core.lib import wp_checker
from core.lib import wp_request
from core.lib import wp_banner
from core.modules import wp_generic
from core.modules import wp_theme
from core.modules import wp_users
from core.modules import wp_plugin
from core.modules import wp_attack
from core.modules import wp_brute

class wpscanner():
    #wpscanner.py class
    print_ = wp_print.WPPrint()
    check_ = wp_checker.WPChecker()
    user_agent = ""
    proxy = None
    cookie = None
    redirect = True
    brute = None
    user = None
    sql = False
    xss = False
    lfi = False
    method = None
    wordlist = None
    query = None
    ##############################
    def __init__(self,kwargs):
        self.kwargs = kwargs
