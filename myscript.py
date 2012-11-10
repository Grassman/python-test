#! /usr/bin/env python
import urllib2
apsUrl='http://localhost:9000/aps'
print 'Requesting data for ' + apsUrl
req = urllib2.Request(url=apsUrl)
f = urllib2.urlopen(req)
print 'Data received: ' + f.read()

