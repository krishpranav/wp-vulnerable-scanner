#!/usr/bin/env python2

#imports
import json
import re
import os
import time
import random
import socket
import sys

Version = '0.2.0'

try:
    import requests
except ImportError:
    print '[+] pip install requests'
    print '[-] you need to install the requests module'
    sys.exit()

try:
    from colorama import Fore, Back, Style

    r = Fore.RED
    g = Fore.GREEN
    w = Fore.WHITE
    b = Fore.BLUE
    y = Fore.YELLOW
    m = Fore.MAGENTA
    res = Style.RESET_ALL

except ImportError:
    print '[*] pip install colorama'
    print '[-] you need to install colorama module'
    sys.exit()


class WpScan():
    def __init__(self):
        try:
            self.url = sys.argv[1]
        except IndexError:
            self.cls()
            self.print_logo()
            self.__option()
            self.exit()
        if self.url.startswith('http://'):
            self.url = self.url.replace('http://', '')
        elif self.url.startswith("https://"):
            self.url = self.url.replace('https://', '')
        else:
            pass
        __kill_ip = self.url
        try:
            ip = socket.gethostbyname(__kill_ip)
            