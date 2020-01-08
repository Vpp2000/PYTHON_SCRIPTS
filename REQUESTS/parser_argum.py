
import argparse

# required arg



parser = argparse.ArgumentParser()
parser.add_argument('--domain', type=str , required=True , help= 'Target domain')
parser.add_argument('--output', type=str , required=False, help= 'Output file')
args = parser.parse_args()
print(args.domain)