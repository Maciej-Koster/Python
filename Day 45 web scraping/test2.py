# from bs4 import BeautifulSoup
# import requests
#
# # requests allows us hold of the data of particular url
#
# respone = requests.get(url="https://news.ycombinator.com/")
# yc = respone.text
#
# soup = BeautifulSoup(yc, "html.parser")
#
# # print(soup.prettify())
#
# article = soup.find_all(name="a", class_='titlelink')
# article_score = [int(score.get_text().split()[0]) for score in soup.find_all(name="span", class_='score')]
#
# article_texts = []
# article_links = []
#
# for artivle_tag in article:
#     text = artivle_tag.get_text()
#     article_texts.append(text)
#
#     link = artivle_tag.get("href")
#     article_links.append(link)
#
# index = article_score.index(max(article_score))
#
#
# print(article_texts[index])
# print(article_links[index])
# print(article_score[index])
