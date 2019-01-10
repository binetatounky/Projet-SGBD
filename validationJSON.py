from pathlib import Path
from os import walk,getcwd
from os.path import join
from json import load
from sys import argv
import json

data = json.load('fichier.json')
def validate(f):
    with open(f) as data:
        try: 
            load(data)
            return True
        except: 
            return False

def main():
    try:
        path = argv[1]
    except:
        path = getcwd()
    print("working dir {0}".format(path))
    json = [join(d, x)
                for d, dirs, files in walk(path)
                for x in files if x.endswith(".json")]
    for f in json:
        if not validate(f):
            print("not valid: {0}".format(f))

if __name__=="__main__":
    main()
