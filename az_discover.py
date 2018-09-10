#!/usr/bin/python
#
import sys
import requests
import socket
import netaddr
import getpass

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def api_call (url, user, password):
    resp = requests.get(url, verify=False, auth=(user,password)).json()
    try: resp['errors']
    except KeyError: return (resp)
    sys.stderr.write ("ERROR: " + resp['errors'][0]['message'] + "\n")
    exit (1)

addr = socket.gethostbyname(sys.argv[2])
url_head = "https://"+ sys.argv[1] + ":8080/platform/3/"
user = raw_input("User: ")
password = getpass.getpass("Password: ")
url = url_head + "network/pools"
pool_data = api_call (url, user, password)
for i, p in enumerate(pool_data['pools']):
    for j, r in enumerate(pool_data['pools'][i]['ranges']):
        ip_range = list (netaddr.iter_iprange(r['low'],r['high']))
        if netaddr.IPAddress(addr) in ip_range:
            zone = p['access_zone']
            url = url_head + "zones"
            zone_data = api_call (url, user, password)
            for z, y in enumerate (zone_data['zones']):
                if y['id'] == zone:
                    print "Zone: " + zone
                    print "Root Path: " + y['path']
                    exit (0)

sys.stderr.write ("ERROR: Zone not found\n")

