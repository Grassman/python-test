#! /usr/bin/env python
import dbus

bus = dbus.SystemBus()
remote_object = bus.get_object("org.freedesktop.DBus","/org/freedesktop/DBus")
iface = dbus.Interface(remote_object, "org.freedesktop.DBus")
print iface.ListNames()

