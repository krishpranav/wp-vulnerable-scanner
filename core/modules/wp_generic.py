#!/usr/bin/env/pyth

from core.lib import wp_checker
from core.lib import wp_colors
from core.lib import wp_print
from core.lib import wp_request
import re
import requests 
import json 

class WPGeneric:
	"""WordPress Generic Checks"""
	check_ = wp_checker.WPChecker()
	print_ = wp_print.WPPrint()
	def __init__(self,agent,proxy,redirect,url):
		self.url = url
		# request 
		self.req = wp_request.WPRequest(agent=agent,proxy=proxy,redir=redirect)

	def xmlrpc(self):
        #self function
		# Check xmlrpc.php 
		try:
			url = self.check_.check(self.url,"/xmlrpc.php")
			# return html,url,code and info 
			html,uri,code,info = self.req.Send(url) 
			if html and code == 405:
				self.print_.aprint("XML-RPC Interface available under: {}".format(uri))
		except Exception as e:
			pass