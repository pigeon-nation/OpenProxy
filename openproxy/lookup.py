#!/usr/bin/env python3

import requests
import certifi

import pprint

#url = 'https://api.npoint.io/a9f5f7262f664d6c531e'
url = 'https://api.npoint.io/7ac43994b62898699769'
req = requests.get(url, verify=certifi.where())
dat = req.json()

def filter(dat=dat, **kwargs):
	filtered = []
	servers = dat['data']
	
	for server in servers:
		validated = True
		for kwarg in kwargs.keys():
			if not kwargs[kwarg] == server[kwarg]:
				validated = False
		
		if validated:
			filtered.append(server)
	
	return filtered

def get_secondary(request='getproxies', protocol='http', timeout='10000', country='all', ssl='all', anonymity='elite'):
	# getporxies can be displayproxies if wish is to display in browser
	endpoint = 'https://api.proxyscrape.com/v2/'
	configs = f'?request={request}&protocol={protocol}&timeout={timeout}&country={country}&ssl={ssl}&anonymity={anonymity}'
	
	proxidx = endpoint + configs
	return requests.get(proxidx, verify=certifi.where()).content.decode()