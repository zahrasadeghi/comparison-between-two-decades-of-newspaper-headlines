from persian_wordcloud.wordcloud import PersianWordCloud
from PIL import Image
import numpy as np
import json
from collections import Counter, OrderedDict

def getMin(data):
    minlist = {}
    j=0
    for i in data.keys():
        if j>len(data)-150 and data[i]>0:
            minlist[i] = 1/data[i]
        j = j+1
    return minlist
data = json.load(open("data set/76_85.txt"))
print(data)
data = OrderedDict(data)
data = getMin(data)
print(data)
wordcloud = PersianWordCloud(
    only_persian=True,
    max_words=100,
    margin=0,
    width=800,
    height=800,
    min_font_size=1,
    max_font_size=500,
    background_color="black",
).generate_from_frequencies(frequencies=data)
image = wordcloud.to_image()
image.show()
image.save('76_85minDis.png')
