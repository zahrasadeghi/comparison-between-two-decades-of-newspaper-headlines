# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from collections import Counter, OrderedDict
from arabic_reshaper import arabic_reshaper
from bidi.algorithm import get_display
from persian_wordcloud.wordcloud import PersianWordCloud
import json
from PersianStemmer import PersianStemmer


stopWords = open("../stopWords.txt", 'r+').read().split("\n")
ps = PersianStemmer()

def reshape(data):
    data2 = {}
    for i in data.keys():
        if i not in stopWords:
            data2[get_display(arabic_reshaper.reshape(ps.run(i)))] = data[i]
    return data2


def removeStopWords(data):
#     stopWords = ["و", "در", "با", "از", "بر", "ها", "های", "می", "برای", "شد", "است", "،", "به",
#                  "|", "ا", "را", "ایران", "صفحه", "مشاهده", "متن", "[PDF]",
#                  "این", "تهران", "است.", 'خواهد', "کرده", "شده", "کند", "ی", "ها", "حقوق", "محفوظ", "متعلق", "است",
#                  "سياست","اجتماعی","اقتصادی","دانش", "فناوری","هنر","بـورس","زادبوم","حوادث","خارجی","فرهنگ و آموزش",
#                  "سياسی","شهر", "تماشا","سلامت","شهری","راهنما","ورزش","صفحه","آخر","ضميمه","|",
#                  "ﻦﯿﺑ","ﯽﮔﺪﻧﺯ","ﯼﺮﻬﺸﻤﻫ","ﯽﺳﺎﯿﺳ","آموزش","آرشیو","ﻪﻤﯿﻤﺿ" ,"شهرآرا"]
    cleanStopWords = []
    for i in stopWords:
        cleanStopWords.append(get_display(arabic_reshaper.reshape(i)))

    for word in stopWords:
        data[word] = 0
    for i in data.keys():
        if len(i)<3:
            data[i] = 0
    return data

def calculateRelativePercent(data, filename):
    data2 = {}
    for word in data.keys():
        data2[word] = float(data[word])/4051049

    json.dump(data, open(filename[:-3]+"clean.second.txt", 'w'))

def cleanData(filename):
    file = open(filename, 'r+')
    text = file.read().replace("\n", " ").replace("‌", " ").replace("\r", " ").replace("‎", "").replace("‏", "")
    text = PersianWordCloud.remove_ar(text)
    text = text.split(" ")
    counter = Counter(text)
    calculateRelativePercent(OrderedDict(counter.most_common()),filename)
    data = OrderedDict(counter.most_common(300))
    allWords = sum(counter.values())
    print(allWords)
    # data["تعداد کل لغات = "] = allWords
    data = reshape(data)
    data = removeStopWords(data)
    newdict = {}
    for i in data.keys():
        if data[i] != 0:
            newdict[i] = data[i]
    print(len(newdict))
    json.dump(newdict, open(filename[:-3]+"cleaner.txt", 'w'))


cleanData("../data set/1376.txt")
cleanData("../data set/1385.txt")
