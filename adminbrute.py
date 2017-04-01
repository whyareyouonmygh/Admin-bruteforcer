from urllib2 import Request, urlopen, URLError, HTTPError
from sys import argv
import re
def a():
	f = open("link.txt","r")
	l = argv[1]
	while True:
		sl = f.readline()
		if not sl:
			break
		rl = "http://"+l+"/"+sl
		r = Request(rl)
		try:
			re = urlopen(r)
			rd = re.read()
			print "Trying ",rl
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			if rd.find("Username") != -1 or rd.find("username") != -1 or rd.find("USERNAME") != -1 or rd.find("Password") != -1 or rd.find("password") != -1 or rd.find("PASSWORD") != -1 or rd.find("Admin Login") != -1 or rd.find("admin login") != -1 or rd.find("ADMIN LOGIN") != -1 or rd.find("Admin Log In") != -1 or rd.find("admin log in") != -1 or rd.find("ADMIN LOG IN") != -1 or rd.find("Admin Log-in") != -1 or rd.find("admin log-in") != -1 or rd.find("ADMIN LOG-IN") != -1:
				print "Possible admin page> ",rl
a()