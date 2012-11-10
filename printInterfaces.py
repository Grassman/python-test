#!/usr/bin/python
# -*- coding: utf-8 -*-

import dbus
import MySQLdb as mdb
import sys

con = None
cur = None

def createTable():
	cur.execute("CREATE TABLE IF NOT EXISTS Accesspoints(Id INT PRIMARY KEY AUTO_INCREMENT, SSID VARCHAR(255), MAC VARCHAR(255), ENCRYPTED VARCHAR(255))")

def persistAp(ssid, mac, encrypted):
        cur.execute("SELECT * FROM Accesspoints WHERE MAC='"+mac+"'")
        rows = cur.fetchall()
	if len(rows) == 0:
		cur.execute("INSERT INTO Accesspoints(SSID, MAC, ENCRYPTED) VALUES('"+ssid+"','"+mac+"','"+encrypted+"')")
	else:
	    	print "AP with MAC='" + mac + "' already added"

def printApTable():
	cur.execute("SELECT * FROM Accesspoints")
	rows=cur.fetchall()
        print 'Rows found: '
        for row in rows:
		print "%2s %3s %4s %5s" % row 

def findAps():
	bus = dbus.SystemBus()

	proxy = bus.get_object("org.freedesktop.NetworkManager", "/org/freedesktop/NetworkManager")
	manager = dbus.Interface(proxy, "org.freedesktop.NetworkManager")

	# Get device-specific state
	devices = manager.GetDevices()
	#for d in devices:
    	#	dev_proxy = bus.get_object("org.freedesktop.NetworkManager", d)
    	#	prop_iface = dbus.Interface(dev_proxy, "org.freedesktop.DBus.Properties")
	persistAp('ssid','mac','YES');
	persistAp('ssid2','mac2','NO');
    	#name = prop_iface.Get("org.freedesktop.NetworkManager.Device", "Interface")
    	#print 'Interface: ' + name + ' found.'
 
if __name__ == "__main__":
        con = mdb.connect('localhost', 'test', 'test666', 'test')
        with con:
                cur = con.cursor()
        createTable()
        findAps()
	con.commit()
        printApTable()
        con.close()
