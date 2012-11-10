import json
import urllib2
import sys

def sendJson(postUrl,ssid,mac,encrypted):
	data = {'ssid': ssid, 'mac': mac, 'encrypted': encrypted}
	req = urllib2.Request(postUrl, json.dumps(data), {'Content-Type': 'application/json'})
	f = urllib2.urlopen(req)
	response = f.read()
	f.close()
if __name__ == "__main__":
    sendJson(sys.argv[1], "SSID", "MAC!", "NO")
