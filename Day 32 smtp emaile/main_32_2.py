import smtplib
import datetime as dt
import random
import keys

now = dt.datetime.now()
day = now.weekday()

with open("quotes.txt", "r") as file:
    list_of_quotes = file.readlines()
random_quote = random.choice(list_of_quotes)

my_email = keys.test_email_1
password = keys.password_test_email_1

if day == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() # włączenie zabezpieczenia, standard tls
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=keys.my_email_gmail,
            to_addrs="testowyemail885@gmail.com",
            msg=f"Subject: Hello\n\n{random_quote}"
        )
else:
    print("zły dzień")