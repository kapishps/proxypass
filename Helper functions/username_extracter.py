__author__ = 'kapish'
from bs4 import BeautifulSoup
html_doc = open('../html/44_html.html', 'r')
soup = BeautifulSoup(html_doc,'html.parser')
f = open('../Temp/44_usernames.txt', 'w')
for link in soup.find_all('a'):
    if link.has_attr('href'):
        str= link['href']
        print str[32:]
        f.write("%s\n" % str[32:])
