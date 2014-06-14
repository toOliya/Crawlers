#!/usr/bin/python

import os
import re
import sys
import urllib2


def read_urls(sourceCode, outFile):
# find links in source code, follow them and write the content into output file

	fOut = open(outFile, 'w+')
	
	getLinks = re.findall(r'(<a href=\")(.+html*)\"', sourceCode)	# regex that looks for href that ends in htm(l)
	for link in getLinks:
#		print link[1]

		response = urllib2.urlopen(link[1])
#	print name
		page_source = response.read()
		fOut.write(page_source)
	
	fOut.close()


def openAnything(source):
# make sure we can read from file or url
	try:
		u = urllib2.urlopen(source)
		return u.read()

	except (ValueError, IOError, OSError):
		f = open(source, 'rU')
		content = f.read()
		f.close()

		return content 
		


def main():
	args = sys.argv[1:]	# list of input arguments

	if not args:
		print 'usage: [input_file/url] output_file'
		sys.exit(1)

	sourceCode = openAnything(args[0])

	read_urls(sourceCode, args[1])

	

if __name__ == '__main__':
  main()



