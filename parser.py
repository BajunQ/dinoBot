from lxml import html
import requests as req
import csv

print('Подождите пока загружаются данные с сайта')
table = []
domain = 'http://94.231.164.165'
page = 'hg.htm'
group, grClass, link, place =  '', '', '', ''

def request(domain, page):
    url = '%s/%s' % (domain, page)
    r = req.get(url)
    return r.text

text = request(domain, page)

def start():
                print('ИДЕТ ПАРСИНГ')
                tree = html.fromstring(text)
                date = tree.xpath('//li[@class = "zgr"]/text()')
                group = (tree.xpath('//td[@class = "hd"]/a/text()'))
                grClass = (tree.xpath('//td[@class="ur"]/a[@class="z1"]/text()'))
                place = (tree.xpath('//td[@class="ur"]/a[@class="z2"]/text()'))
                link = (tree.xpath('//td[@class="ur"]/a[@class="z1"]/@href'))
                date = ''.join(date)
                date=date[:10]
                
                for i in range(len(link)):
                    n = i * 2 - 28
                    if(n%10 and n > 0 and n <=100):
                        print('#', end='')
                    checkIfEqual(link[i], date, group, place[i])

def checkIfEqual(link, date, group, place):
            fGr, fD = 0, 0
            text = request(domain, link)
            tree = html.fromstring(text)
            pg = tree.xpath('//td[@class = "vp"]/text()')
            nameClass = tree.xpath('//li[@class = "zgr"]/text()')
            nameClass = ''.join(nameClass)
            
            for i in range(len(pg)):
                for f in range(len(group)):
                    if pg[i] == group[f]:
                        foundGr = group[f]
                        foundPl = place
                        fGr = 1
                        break
            for i in range(len(pg)):
                if pg[i] == date:
                    fD = 1
                    break


            if fGr and fD:
                table.append([foundGr, nameClass, foundPl])
                
   
start()

with open('class.csv', "w", newline="") as file:
    writer = csv.writer(file)
    for i in range(len(table)):
        writer.writerow(table[i])


