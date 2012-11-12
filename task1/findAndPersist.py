#!/usr/bin/python
# -*- coding: utf-8 -*-

import dbus
import MySQLdb as mdb
import sys

con = None
cur = None

def create_table():
	cur.execute("CREATE TABLE IF NOT EXISTS Accesspoints(Id INT PRIMARY KEY AUTO_INCREMENT, SSID VARCHAR(255), MAC VARCHAR(255), ENCRYPTED VARCHAR(255))")

def persist_ap(ssid, mac, encrypted):
        cur.execute("SELECT * FROM Accesspoints WHERE MAC='"+mac+"'")
        rows = cur.fetchall()
	if len(rows) == 0:
		cur.execute("INSERT INTO Accesspoints(SSID, MAC, ENCRYPTED) VALUES('"+ssid+"','"+mac+"','"+encrypted+"')")
	else:
	    	print "AP with MAC='" + mac + "' already added"

def print_ap_table():
	cur.execute("SELECT * FROM Accesspoints")
	rows=cur.fetchall()
        print 'Rows found: '
        for row in rows:
		print "%2s %3s %4s %5s" % row 

def find_aps():
	bus = dbus.SystemBus()

	proxy = bus.get_object("org.freedesktop.NetworkManager", "/org/freedesktop/NetworkManager")
	manager = dbus.Interface(proxy, "org.freedesktop.NetworkManager")

	# Get device-specific state
	devices = manager.GetDevices()
	for d in devices:
    		device_proxy = bus.get_object("org.freedesktop.NetworkManager", d)
    		prop_iface = dbus.Interface(device_proxy, "org.freedesktop.DBus.Properties")
    		name = prop_iface.Get("org.freedesktop.NetworkManager.Device", "Interface")
	        deviceType = prop_iface.Get("org.freedesktop.NetworkManager.Device", "deviceType")
    		print 'Interface: ' + name  
		if deviceType == 2:
			print 'It is wifi!'
			accesspoints = device_proxy.GetAccessPoints(dbus_interface='org.freedesktop.NetworkManager.Device.Wireless')
			for ap in accesspoints:
				ap_proxy = bus.get_object("org.freedesktop.NetworkManager.Device.Wireless", ap)
				ap_prop_if = dbus.Interface(dev_proxy, "org.freedesktop.DBus.Properties")
				ssid = ap_prop_if.Get("org.freedesktop.NetworkManager.AccessPoint","ssid")
				mac = ap_prop_if.Get("org.freedesktop.NetworkManager.AccessPoint","HwAddress")
				wpaflag = ap_prop_if.Get("org.freedesktop.NetworkManager.AccessPoint","WpaFlags")
				encrypted = "No"
				if wpaflag > 0:
					encrypted = "Yes"
				print 'Persisting ' + ssid + ', ' + mac + ', ' + encrypted
				#persist_ap(ssid,mac,encrypted)
 
if __name__ == "__main__":
        #con = mdb.connect('localhost', 'test', 'test666', 'test')
        #with con:
        #        cur = con.cursor()
        #create_table()
        find_aps()
	#con.commit()
        #print_ap_table()
        #con.close()
