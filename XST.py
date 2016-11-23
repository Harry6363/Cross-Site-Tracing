#!/usr/bin/env python
import requests
verbs = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'TRACE',
'TEST']
URL = raw_input("Entr url: ")
for verb in verbs:
 req = requests.request(verb, URL)
print verb, req.status_code, req.reason
if verb == 'TRACE' and 'TRACE / HTTP/1.1' in req.text:
   print 'Possible Cross Site Tracing vulnerability found'
