#1st Day

The problem that I coded was a Data joyrney bite from pybites. I choose the data journey because I, as a statistician, 
am more confortable in dealing with data.

The problem was to get some data from cars models and automakers and extract some data from it. Pretty simple!
Well, at first I tough on using pandas, but then I decided to try the less confortable way and go with the 
solution without using pandas.

It was fun, and not exactly easy at first. This just showed me how it is good to be doing this challenge and learn to 
code better. I coded a solution that didn't seem to work on the pytests, but it did give the solution for the problem.

So, here are both solutions:

- My solution:
```
from collections import Counter

import requests

CAR_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/cars.json'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()

print()


# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    pass
    filt_year = list(filter(lambda date: date['year'] == year, data))
    maker = [k['automaker'] for k in filt_year if k.get('automaker')]
    c = Counter(maker).most_common()
    for k, v in c:
        return print(k)




def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    pass
    maker = list(filter(lambda manufacter: manufacter['automaker'] == automaker, data))
    res = list(filter(lambda date: date['year'] == year, maker))
    return print(res)
```

- Pybites solution:

```

from collections import Counter

import requests

CAR_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/cars.json'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()


# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    cnt = Counter(row["automaker"] for row in data
                  if row["year"] == year).most_common()
    return cnt[0][0]


def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    return set([row["model"] for row in data
                if row["automaker"] == automaker and
                row["year"] == year])

```


My code didn't test right, I don't really know why though. ~~I'll look at it later!! :grinning:~~

Tomorrow it's a new challenge!!!





