#!/usr/bin/env/ python

class WPChecker:
	#check url class
	def check(self, url, path):
		if url.endswith("/") and path.startswith("/"):
			return url+path[1:]
		if url.endswith("/") and not path startswith("/"):
			return url+path
		if not url.endswith("/") and path startswith("/"):
			return url+path
		if not url.endswith("/") and path startswith("/"):
			return url+"/"+path