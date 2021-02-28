#!/usr/bin/env python2

#imports
import json
import re
import os
import time
import random
import socket
import sys

#default version
Version = '0.2.0'

#trying a test to check all modules are pre installed
try:
    import requests
#if not it will raise a error
except ImportError:
    print '[+] pip install requests'
    print '[-] you need to install the requests module'
    sys.exit()

#function for setting color
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

#main class for wpscan tool
class WpScan():
    #this def function contains only self
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
            self.CheckWordpress = requests.get('http://' + self.url, timeout=5)
            if '/wp-content/' in self.CheckWordpress.text:
                self.cls()
                self.print_logo()
                print r + '    [' + y + '+' + r + ']' + w + ' URL      : ' + m + self.url
                print r + '    [' + y + '+' + r + ']' + w + ' IP Server: ' + m + ip
                print r + '    [' + y + '+' + r + ']' + w + ' Server   : ' + m + self.CheckWordpress.headers[ 'server']
                self.UserName_Enumeration()
                self.CpaNel_UserName_Enumeration()
                self.Version_Wp()
                self.GeT_Theme_Name()
                self.GeT_PluGin_Name()
            else:
                self.cls()
                self.print_logo()
                self.Wrong2()
                sys.exit()
        except socket.gaierror:
             self.cls()
            self.print_logo()
            print y + '---------------------------------------------------'
            print g + '    [' + y + '+' + g + ']' + r + ' Error: ' + y + '    [ ' + w + \
                  ' Something worng! target.com without / in end ' + y + ']'
            sys.exit()
        except requests.exceptions.ReadTimeout:
            self.cls()
            self.print_logo()
            print y + '---------------------------------------------------'
            print g + '    [' + y + '+' + g + ']' + r + ' Error: ' + y + '    [ ' + w + \
                ' ConnectionError! Maybe server Down, Or your ip blocked! ' + y + ']'
           
    def __option(self):
        try:
            print y + '---------------------------------------------------'
            print r + '    [' + y + '+' + r + ']' + w + ' usage: ' + g + '    [ ' \
                + w + ' Python wp-vuln-scanner.py Domain.com ' + g + ']'
        except:
            pass

        