#! /usr/bin/env python
import urllib2
import sys

apsUrl=sys.argv[1]
print 'Requesting data for ' + apsUrl
req = urllib2.Request(url=apsUrl)
f = urllib2.urlopen(req)
print 'Data received: ' + f.read()

