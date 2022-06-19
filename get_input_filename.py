import os

env_file = os.getenv('GITHUB_ENV')

with open(env_file, "a") as myfile:
    myfile.write("inputfile=input/"+os.listdir("input")[1])