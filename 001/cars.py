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

get_models('Mercedes-Benz', 2007)

most_prolific_automaker(1999)
