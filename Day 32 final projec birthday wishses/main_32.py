##################### Extra Hard Starting Project ######################
import pandas
import smtplib
import datetime as dt
import random
import os
import smtplib
import keys

birthwishes = pandas.read_csv("birthdays.csv")

# 1. Update the birthdays.csv
decyzja = input("Chcesz zapisac date urodzin? tak/nie: ").lower()
if(decyzja == "tak"):
    rows = len(birthwishes.index)
    for x in birthwishes:
        dane = input(f"Podaj {x}: ")
        birthwishes.loc[rows, x] = dane
    birthwishes.to_csv("birthdays.csv")

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
day = now.day
month = now.month

dobry_miesiac = []
zyczenia_komu = []
if month in birthwishes.values:
    for i in range(len(birthwishes.index)):
        if birthwishes["month"][i] == month:
            dobry_miesiac.append(i)
    for item in dobry_miesiac:
        if birthwishes["day"][item] == day:
            zyczenia_komu.append(item)
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
arr = os.listdir("letter_templates")
zyczenia = random.choice(arr)
with open(f"letter_templates/{zyczenia}", "r") as file:
    text = file.read()

imie = []
for item in birthwishes['name'][zyczenia_komu]:
    imie.append(item)

text = text.replace("[NAME]", f"{imie[0]}")

# 4. Send the letter generated in step 3 to that person's email address.

my_email = keys.test_email_1
password = keys.password_test_email_1

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()  # włączenie zabezpieczenia, standard tls
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=keys.my_email_gmail,
        msg=f"Subject: Hello\n\n{text}"
    )


