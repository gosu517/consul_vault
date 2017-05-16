#!/bin/python

# Usage: This script helps to identify the active node as the only returnable node when
# clients request vault servers from consul.

import os
import sys
import requests
import json

def getHealthCode():
  payload = {"standbycode":"400"}
  r = requests.get(verify=False,url='https://127.0.0.1:8200/v1/sys/health', params=payload)
  results = r.json()
  return results["standby"]

def run():
  if getHealthCode():
    print "standby"
    exit(2)
  else:
    print "Active"
    exit(0)

if __name__ == "__main__":
  run()
