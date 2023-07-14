#!/usr/bin/env python3

import requests
import random

from .lookup import filter, dat

def format(method, ip, port):
	return method + '://' + ip + ':' + port

def fetch(url, proxy, fmt='https', **kwargs):
	return requests.get(url, proxies={fmt: proxy}, **kwargs)

def random_fetch(url, **kwargs):
	good_proxys = filter(anonymityLevel='elite', speed=1)
	trycount = 0
	
	while 1:
		proxy = random.choice(good_proxys)
		endpoint = format('https', proxy['ip'], proxy['port'])
		data = None
		
		try:
			data = fetch(url, endpoint, 'socks', **kwargs)
		except:
			trycount += 1
		else:
			break
	
	return data, proxy, trycount
