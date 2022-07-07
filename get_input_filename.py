import os

import argparse
#import os 
parser=argparse.ArgumentParser(description="io files")

parser.add_argument("newfile",  help="newfile")

args=parser.parse_args()
env_file = os.getenv('GITHUB_ENV')

with open(env_file, "a") as myfile:
    myfile.write("inputfile="+args.newfile[1:-1].split(',')[-1][1:-1])