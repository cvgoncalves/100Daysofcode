import json
from pathlib import Path
from urllib.request import urlretrieve
import re

TMP = Path('/tmp')
S3 = 'https://bites-data.s3.us-east-2.amazonaws.com/'
DATA = 'omdb_data'

DATA_LOCAL = TMP / DATA
if not Path(DATA_LOCAL).exists():
    urlretrieve(S3 + DATA, DATA_LOCAL)

def movies():
    files = []
    with open(DATA_LOCAL) as f:
        for i, line in enumerate(f.readlines(), 1):
            movies_json = TMP / f'{i}.json'
            with open(movies_json, 'w') as f:
                f.write(f'{line}\n')
            files.append(movies_json)
    return files

files = movies()

def get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""
    movies_list = []
    for movie in files:
        with open(movie) as json_file:
            data = json.load(json_file)
            movies_list.append(data)
    return movies_list

#print(get_movie_data(files))


movies = get_movie_data(files)

for m in movies:
    print(m)

def get_single_comedy(movies: list) -> str:
    """return the movie with Comedy in Genres"""
    for i in movies:
        spl = i['Genre'].split(',')
        if 'Comedy' in spl:
            genre = i['Title']
            return genre

print(get_single_comedy(movies))


def get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""
    nom = 0
    for m in movies:
        s = m['Awards'].split(',')
        for i in s:
            t = [int(i) for i in re.findall(r'\b\d+\b', i)]
            if len(t) > 2:
                w = [t[1], t[0] + t[2]]
            else:
                w = t
            if w[1] > nom:
                nom = w[1]
                name = m['Title']
            else:
                nom = nom
                name = name
    return name

print(get_movie_most_nominations(movies))



def get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""
    runtime = 0
    for m in movies:
        s = m['Runtime'].split(',')
        for i in s:
            t = [int(i) for i in re.findall(r'\b\d+\b', i)]
            if t[0] > runtime:
                runtime = t[0]
                name = m['Title']
            else:
                runtime = runtime
                name = name
    return name


print(get_movie_longest_runtime(movies))