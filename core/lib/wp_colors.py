#!/usr/bin/env python

class WPColors:
	#simple colors list
	def red(self,num):
		return "\033["+str(num)+";31m"

	def end(self):
		#reset color
		return "\033[0m"