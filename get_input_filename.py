import os

import argparse
#import os 
parser=argparse.ArgumentParser(description="io files")

parser.add_argument("newfile",  help="newfile")

args=parser.parse_args()
print('hi')
print(args.newfile)
print('bye')
env_file = os.getenv('GITHUB_ENV')

with open(env_file, "a") as myfile:
    myfile.write(args.newfile[-1])