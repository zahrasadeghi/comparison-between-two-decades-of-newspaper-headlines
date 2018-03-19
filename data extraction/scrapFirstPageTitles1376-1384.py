import urllib2
from bs4 import BeautifulSoup
import requests

file = open('/Users/zahra/Documents/GitHub/nlp-hw2/2/dataSet/85firstPage1-2.txt', 'a')

def findLinksOfDays(yearlink):
    yearPage = urllib2.urlopen(yearlink)
    soup = BeautifulSoup(yearPage, 'html.parser')
    daysLinks = soup.find_all("a")
    finalDaysLinks = []
    for daylink in daysLinks:
        daylink = daylink.get("href")
        finalDaysLinks.append(str("http://www.hamshahrionline.ir/hamnews/13" + daylink[0] + daylink[1] + "/" + daylink))
    return finalDaysLinks


def findFirstPageTitles(daylink):
    request = requests.get(daylink)
    if request.status_code == 200:
        page = urllib2.urlopen(daylink)
        soup = BeautifulSoup(page, 'html.parser')
        firstPageTitles = soup.find_all('td', attrs={"align": "center" })
        titles = ""
        for title in range(0, len(firstPageTitles)):
            titles = titles + " " + (firstPageTitles[title].text.strip())
        file.write(titles.encode('utf8'))
        return titles
    else:
        return ""



def findDataOfADay(daylink):
    return findFirstPageTitles(daylink)


def findDataOfAYear(yearLink):
    daysLinks = findLinksOfDays(yearLink)
    texts = ""
    for daylink in daysLinks:
        texts = texts + " " + findDataOfADay(daylink)
    print texts.replace("\n","")
    return texts


yearsLinks = []
dataOfTheYear = {}

for i in range(85, 86):
    yearsLinks.append(str("http://www.hamshahrionline.ir/hamnews/13" + str(i) + "/arch" + str(i) + ".htm"))

year = 85
for yearlink in yearsLinks:
    print year
    dataOfTheYear[year] = findDataOfAYear(yearlink)
    for i in dataOfTheYear[year]:
         for j in i:
             file.write(j.encode('utf8'))
    break
    # firstPage = open('/Users/zahra/Documents/GitHub/nlp-hw2/data set/76firstPage1-2.txt', 'w+')
    # #OtherPage = open('/Users/zahra/Desktop/ newspaper/13'+str(i+75)+'/otherPage0::10.txt', 'w+')
    # data = findInfoOfAYear(yearlink)
    # # for i in data["other pages"]:
    # #     for j in i:
    # #         for k in j:
    # #             OtherPage.write(k.replace("\n", " ").encode('utf8'))
    # for i in data["first page"]:
    #     for j in i:
    #         firstPage.write(j.encode('utf8'))
    # break


# print(soup.a)
