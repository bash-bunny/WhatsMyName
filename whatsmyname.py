#!/urs/bin/env python

import sys
import json
import requests
import threading

def check_url(url, e_code, e_string):
	try:
		r = requests.get(url, timeout=30)
		if(r.status_code == e_code):
			if(e_string in r.text):
				print(url)
	except:
		pass

def main():
	# Checking if there are the correct parameters
	if(len(sys.argv) != 2):
		print("Usage: python whatsmyname.py username")
		exit(1)

	# Get the username
	user = sys.argv[1]

	# Opening JSON file
	f = open('wmn-data.json')

	# returns JSON object as
	# a dictionary
	data = json.load(f)

	# Check every url
	for site in data['sites']:
		url = site['uri_check'].replace("{account}", user)
		e_code = site['e_code']
		e_string = site['e_string']
		threading.Thread(target=check_url, args=(url,e_code,e_string)).start()

if __name__ == "__main__":
    main()
