#!/usr/bin/env python

#imports
import re
import sys
import urllib
from core.lib import wp_checker
from core.lib import wp_colors
from core.lib import wp_print
from core.lib import wp_request

class WPAttack:
	#attack
	check_ = wp_checker.WPChecker()
	print_ = wp_print.WPPrint()

	#main init
	def __init__(self,agent,proxy,redirect,url,method,payload):
		self.url = url
		self.method = method
		self.payload = payload
		# requests
		self.req = wp_request.WPRequest(agent=agent,proxy=proxy,redir=redirect)

	def xss(self):
		# Simple testing xss vulns
		self.print_.aprint("Testing xss vulns...")
		print ""
		# self.payload ==> {'id':2,'cat':2}
		params = dict([x.split("=") for x in self.payload.split("&")])
		param = {}
		# open file core/db/wpxss.txt, mode read
		db = open("core/db/wpxss.txt","rb")
		file = [x.split("\n") for x in db]
		try:
			for item in params.items():
				for x in file:
					# 
					param[item[0]]=item[1].replace(item[1],x[0])
					# encode payload
					enparam = urllib.urlencode(param)
					# check url 
					url = self.check_.check(self.url,"")
					# return data,url,code and headers
					html,uri,code,info = self.req.Send(url,self.method,enparam)
					# search payload in html
					if re.search(x[0],html) and code == 200:
						print "%s[%s][%s][vuln]%s %s"%(wp_colors.WPColors().red(1),code,self.method,wp_colors.WPColors().end(),uri)
					else:
						print "%s[%s][%s][not vuln]%s %s"%(wp_colors.WPColors().green(1),code,self.method,wp_colors.WPColors().end(),uri)
					# return original data 
					param[item[0]] = item[1].replace(x[0],item[1])
		except Exception,err:
			pass
		sys.exit()