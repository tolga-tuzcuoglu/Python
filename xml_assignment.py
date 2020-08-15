import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

# url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
url = 'http://py4e-data.dr-chuck.net/comments_784885.xml'
urlopen = urllib.request.urlopen(url)
data = urlopen.read()
tree = ET.fromstring(data)

results = tree.findall('comments/comment')

sum=0

for item in results:
    x = item.find('count').text
    x = int(x)
    sum = sum + x
print(sum)
