from bs4 import BeautifulSoup
import requests


'date = input("What year you would like to travel in YYYY-MM-DD format:")


response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movies_text = response.text

soup = BeautifulSoup(movies_text, "html.parser")

movies = soup.find_all(name="h3", class_="title")

# print(movies[0].get_text())
movies_list = [item.get_text() for item in movies]
movies_list.reverse()
# print(movies_list)

with open("movies.txt", mode="w") as file:
    for item in movies_list:
        file.write(item + "\n")