# az_discover
Quick Isilon PAPI script to discover the access zone given an IP address

Syntax: az_discover.py API_name_or_IP name_or_IP

API_NAME_or_IP is a hostname or IP of an address in the System Zone from which to make the API call
name_or_IP is a hostname or IP that you wish to discover the access zone

The script returns the zone name and the base path of the zone.

Example:

$ ./az_discover.py isilon 172.16.9.30
User: root
Password: 
Zone: zone2
Root Path: /ifs/zone2
