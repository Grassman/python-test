#! /usr/bin/env python
import urllib2
print 'Requesting data for http://localhost:9000/pipe/PipeIt/latest'
req = urllib2.Request(url='http://localhost:9000/pipe/PipeIt/latest')
f = urllib2.urlopen(req)
print 'Data received: ' + f.read()

