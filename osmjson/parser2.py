import sys

def parseLine(curLine):
    fieldList = curLine.split()

    #If this is a end tag
    if len(fieldList) == 1:
        return
    
    return {
        fieldList[0],
    }

toRet = {}



for line in open(sys.argv[1], 'r'):
    parseLine(line)

