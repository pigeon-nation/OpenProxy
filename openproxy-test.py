import openproxy
import openproxy.lookup

heading = '''
░█▀▀▀█ █▀▀█ █▀▀ █▀▀▄ ░█▀▀█ █▀▀█ █▀▀█ █─█ █──█
░█──░█ █──█ █▀▀ █──█ ░█▄▄█ █▄▄▀ █──█ ▄▀▄ █▄▄█       ▀█▀ █▀▀ █▀ ▀█▀ █▀▀ █▀█
░█▄▄▄█ █▀▀▀ ▀▀▀ ▀──▀ ░█─── ▀─▀▀ ▀▀▀▀ ▀─▀ ▄▄▄█ v1.2  ░█░ ██▄ ▄█ ░█░ ██▄ █▀▄ v1.0
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄'''

print(heading)
print()
print('This is free software, distributed under an MIT License. ')
print('This software is currently in beta testing versions. ')
print('This software is authored by Pigeon Nation.')
print()
print('---------------------------')
print('Enter 0 to connect to a random server, 1 to connect to a specific server, and 2 to exit. ')
print('_ will give you a list of other proxy servers. ')
print('Enter your command below: ')
print()

while 1:
	cmd = input(' >> ')
	
	if cmd == '0':
		try:
			code = openproxy.random_fetch(input('Enter URL > '))[0].content.decode()
		except:
			print('Unknown Error. ')
		print(code)
	elif cmd == '1':
		endpt = input('Enter Full Endpoint > ')
		config = input('Enter Protocol (Usually "socks") > ')
		try:
			code = openproxy.fetch(input('Enter URL > '), endpt, config).content.decode()
		except:
			print('Connection Error. ')
		else:
			print(code)
	elif cmd == '2':
		break
	elif cmd == '_':
		print()
		print('Some HTTP Proxies: ')
		print(openproxy.lookup.get_secondary())
	else:
		print('Command Not Found. ')

'''ip = '1.171.24.199'
port = '3128'
endpoint = 'https://1.171.24.199:3128'

print(openproxy.fetch('https://www.example.com/', endpoint))'''