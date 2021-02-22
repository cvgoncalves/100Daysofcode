import os
from collections import Counter
import urllib.request
import xml.etree.ElementTree as ET

# prep
tempfile = os.path.join('/tmp', 'feed')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/feed',
    tempfile
)

with open(tempfile) as f:
    content = f.read().lower()
    root = ET.fromstring(content)

category = []
for child in root:
    for kid in child:
        for item in kid.findall('category'):
            category.append(kid.find('category').text)
c = Counter(category)
c = sorted(c, reverse=True)


def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    tree = ET.fromstring(content)
    tags = (e.text for e in tree.findall("./channel/item/category"))
    return Counter(tags).most_common(n)

print(get_pybites_top_tags(10))