import json
from collections import Counter, OrderedDict

def calculateRelativePercent(filename76, filename85):
    data76 = json.load(open(filename76))
    data76 = OrderedDict(data76)
    data85 = json.load(open(filename85))
    data85 = OrderedDict(data85)
    data76_85 ={}
    data85_76 = {}
    for i in data76.keys():
        if i in data85:
            data76_85[i] = data76[i] - data85[i]
        else:
            data76_85[i] = data76[i]
    for i in data85.keys():
        if i in data76:
            data85_76[i] = data85[i] - data76[i]
        else:
            data85_76[i] = data85[i]
    json.dump(data85_76, open("85_76.txt", 'w'))
    json.dump(data76_85, open("76_85.txt", 'w'))

calculateRelativePercent("../data set/1376.clean.txt","../data set/1385.clean.txt")
