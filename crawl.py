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



def main():
	args = sys.argv[1:]

	if not args:
		print 'usage: input_file output_file'
		sys.exit(1)

	f = open(args[0], 'rU')
	sourceCode = f.read() 

	read_urls(sourceCode, args[1])
	f.close()

	

if __name__ == '__main__':
  main()



