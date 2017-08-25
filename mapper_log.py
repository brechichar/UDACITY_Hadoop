#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
import re

parts = [
    r'(?P<host>\S+)',                   # host %h
    r'\S+',                             # indent %l (unused)
    r'(?P<user>\S+)',                   # user %u
    r'\[(?P<time>.+)\]',                # time %t
    r'"(?P<request>.+)"',               # request "%r"
    r'(?P<status>[0-9]+)',              # status %>s
    r'(?P<size>\S+)',                   # size %b (careful, can be '-')
]
pattern = re.compile(r'\s+'.join(parts)+r'\s*\Z')


for line in sys.stdin:
    #data = line.strip().split("GET ")
    #data = line.strip().split(" ")
    data = pattern.match(line)
    if data is not None:
      res=data.groupdict()
      print "{0}\t{1}".format(res["request"].split(" ")[1],1)

