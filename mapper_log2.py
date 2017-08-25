#!/usr/bin/env python

import sys
import re

pageCounts = {}
p = re.compile("(?P<IP>[\d\.]+)\s(?P<clientID>\S+)\s(?P<uName>\S+)\s\[(?P<TIME>\S+)\s-(?P<Zone>\S+)\]\s\"(?P<Method>\S+)\s(?P<Path>\S+)\s(?P<protocol>\S+)\"\s(?P<status>\S+)\s(?P<bytes>\S+)")
for line in sys.stdin:
     parsed = p.match(line.replace("http://","").replace("www.","").replace("the-associates.co.uk",""))
     if parsed:
          path = parsed.group('Path')
          if pageCounts.has_key(path):
               pageCounts[path] = pageCounts[path] + 1;
          else:
               pageCounts[path] = 1
     #else:
          #print "{0}\t{1}".format("Error",line)
for item in pageCounts.items():
     k,v = item
     print "{0}\t{1}".format(k,v)
