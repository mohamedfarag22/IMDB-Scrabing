
import requests
from bs4 import BeautifulSoup
from itertools import zip_longest
import csv

rate_movie = []
name_movie = []
year_of_movie = []
rank_movie = []

website = requests.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")

soup = BeautifulSoup(website.text, "lxml")

movies = soup.select("td.titleColumn")

#print(len(movies)) == 250

for rate in soup.select('td.posterColumn span[name=ir]'):

    rate_movie.append(rate.attrs.get('data-value'))

for name in soup.select('td.titleColumn a'):

    # =name.replace('.', ''))
    name_movie.append(name.text)

for year in soup.select('td.titleColumn span[class=secondaryInfo]'):

    year_of_movie.append(year.text)

for rank in range(0, len(movies)):

    movie_string = movies[rank].get_text()

    movie = (' '.join(movie_string.split()).replace('.', ''))

    rank_of_movie = movie[:len(str(rank))-(len(movie))]

    rank_movie.append(rank_of_movie)

file_list = [rank_movie, name_movie, year_of_movie, rate_movie]

exported = zip_longest(*file_list)

with open("D:/دبلومة AI/scribing IMDB.csv", "w") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["rank_movie", "name_movie", "year_of_movie", "rate_movie"])
    wr.writerows(exported)
