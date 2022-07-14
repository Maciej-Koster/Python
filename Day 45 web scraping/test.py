# from bs4 import BeautifulSoup
#
#
#
# with open("website.html") as file:
#     content = file.read()
#
# soup = BeautifulSoup(content, "html.parser")
#
# # print(soup.title)
# # print(soup.title.string)
# # print(soup.prettify())
# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     # x = tag.getText()
#     # print(x)
#     # print(tag.get("href"))
#     pass
#
# heading = soup.find(name="h1", id="name")
# # print(heading)
#
# section_headinh = soup.find(name="h3", class_="heading")
# #pojawi się error, bo słowo class jest zareserwowane przez pythona, dlatego argument nazywa sie class_
# # print(section_headinh.text)
#
# company_url = soup.select_one(selector="p a")
# #dziala jak selector w cdd
# # selector a znajdujący sie wewnątrz selectora p
# # jeśli chcemy odnieść się do selektora id, to tak jak w css zaczynamy przez znak #, a klasy .
# print(company_url)