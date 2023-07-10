import requests
from bs4 import BeautifulSoup

URL = "https://www.timeout.com/film/best-movies-of-all-time"

response = requests.get(url=URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="_h3_cuogz_1")

movie_titles = [movie.getText() for movie in all_movies]

movie_titles_clean = [movie.replace("\xa0", " ") for movie in movie_titles]

with open("Movie scrapper\\movies.txt", "w", encoding="utf-8") as file:
    for movie in movie_titles_clean:
        file.write(f"{movie}\n")
