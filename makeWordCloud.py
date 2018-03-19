from persian_wordcloud.wordcloud import PersianWordCloud
from PIL import Image
import numpy as np
import json
from collections import Counter, OrderedDict

d ={1:"fdf", 4:"999"}
json.dump(d, open("clean.txt", 'w'))
data = json.load(open("/Users/zahra/Documents/GitHub/nlp-hw2/3/data set/1385.clean.txt"))
print(data)

data = OrderedDict(data)
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
image.save('1385.png')
