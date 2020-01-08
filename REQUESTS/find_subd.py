import requests
import time
import urllib3
import sys
import argparse
from functools import reduce
import operator

version = 3

def arg_parser():
	parser = argparse.ArgumentParser()
	parser.add_argument('-d','--domain', type=str , required=True , help= 'Target domain')
	parser.add_argument('-o','--output', type=str , required=False, help= 'Output file')
	return(parser.parse_args())

def banner():
	global version
	print ("Name: Buscador de dominios visto en un tutorial ")
	print (f"Version: {version}")


def url_parser(url):
	try:
		host = urllib3.util.url.parse_url(url).host
	except Exception as e:
		print("Invalid domain, try again...")
		sys.exit(1)

	return host		



def write_subsdomains_file(subdomain,output_file):
	with open(output_file,'a') as fp:
		fp.write(subdomain+'\n')
		fp.close()

def main():
	banner()
	subdomain = []
	subs = 	None
	arguments = arg_parser()
	target= url_parser(arguments.domain)
	output=arguments.output
	req = requests.get(f'https://crt.sh?q=%.{target}&output=json')
	for (key,value) in enumerate(req.json()):
		subdomain.append([value['name_value']])
	subdomain = reduce(operator.concat, subdomain)
	subdomain = list(set(subdomain))
	print(subdomain)

main()
