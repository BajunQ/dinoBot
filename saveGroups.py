from lxml import html
import requests as req
import csv

table = []
domain = 'http://94.231.164.165'
page = 'hg.htm'
group = ''

print('LOADING...')
url = '%s/%s' % (domain, page)
text = req.get(url).text

print('PARSING...')
tree = html.fromstring(text)
group = tree.xpath('//td[@class="hd"]/a/text()')

for i in range(len(group)):
    print(group[i])
    table.append([group[i]])

with open('groups.csv', "w", newline="") as file:
    writer = csv.writer(file)
    for i in range(len(table)):
        writer.writerow(table[i])



