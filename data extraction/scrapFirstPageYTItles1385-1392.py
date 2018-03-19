import urllib2
from bs4 import BeautifulSoup
import requests


def findLinksOfDays(yearlink):
    yearPage = urllib2.urlopen(yearlink)
    soup = BeautifulSoup(yearPage, 'html.parser')
    daysLinks = soup.find_all("a", attrs={'class': "archive_link"})
    finalDaysLinks = []
    for daylink in daysLinks:
        daylink = daylink.get("href")
        finalDaysLinks.append(str("http://www.magiran.com/" + daylink))
    return finalDaysLinks


def findFirstPageTitles(daylink):
    request = requests.get(daylink)
    if request.status_code == 200:
        page = urllib2.urlopen(daylink)
        soup = BeautifulSoup(page, 'html.parser')
        firstPageTitles = soup.find_all("td", attrs={"class": "toc_title"})
        titles = ""
        for title in range(0, len(firstPageTitles)):
            titles = titles + " " + (firstPageTitles[title].text.strip())
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
    print texts.replace("\n", "")
    return texts


yearsLinks = []

dataOfTheYear = {}
dataOfTheYear["other pages"] = []
dataOfTheYear["first page"] = []

for i in range(85, 92):
    yearsLinks.append("http://www.magiran.com/nparchive.asp?year=13" + str(i) + "&mgID=2825")

year = 85
for yearlink in yearsLinks:
    print year
    dataOfTheYear[year] = findDataOfAYear(yearlink)
    file = open('/Users/zahra/Documents/GitHub/nlp-hw2/3/dataSet/' + str(year) + 'firstPage1-2.txt', 'w+')
    for i in dataOfTheYear[year]:
        for j in i:
            file.write(j.encode('utf8'))
    break


# print(soup.a)
