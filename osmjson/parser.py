#pip install xmltodict

import xmltodict
import json
import sys

with open(sys.argv[1],'r') as fd:
    doc = xmltodict.parse(fd.read())

outFileName = "".join(sys.argv[1].split('.osm')[:-1]) + ".json"
print(outFileName)

if (len(sys.argv) == 3):
    outFileName = sys.argv[2]

with open(outFileName, 'w') as outfile:
    json.dump(doc, outfile)