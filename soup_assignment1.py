# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
# url = 'http://py4e-data.dr-chuck.net/comments_42.html'
url =  'http://py4e-data.dr-chuck.net/comments_784883.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
sum = 0
tags = soup('span')
for tag in tags:
    x = int((tag.contents[0]))
    sum = sum + x
print(sum)
