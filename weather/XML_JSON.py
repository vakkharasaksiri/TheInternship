# Need additional library by <pip install xmltodict>
import xmltodict
import json
import sys
inputFile = sys.argv[1]

with open(inputFile, 'r') as f:
    xmlData = f.read()

jsonData= json.dumps(xmltodict.parse(xmlData), indent=4)

with open(inputFile[:-4]+".json", 'w') as f:
    f.write(jsonData)
