import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import keys

AMAZON_URL = "https://www.amazon.com/Instant-Pot-Ultra-Quiet-Fast-Heating-Touchscreen/dp/B096BDTVHH?ref_=ast_sto_dp&th=1&psc=1"

header = {
    "Accept-Language": "pl,en-US;q=0.7,en;q=0.3",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
}

response = requests.get(AMAZON_URL, headers=header)

soup = BeautifulSoup(response.text, "lxml")

soup_class = soup.find(class_="a-size-base a-color-price")
item_price = float(soup_class.string[1:])

if item_price <= 150:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=keys.test_email_1, password=keys.password_test_email_1)
        connection.sendmail(
            from_addr=keys.test_email_1,
            to_addrs=keys.my_email_gmail,
            msg=f"Subject: Hello\n\nProdukt jest w szukanej kwocie, cena:{item_price}, link:{AMAZON_URL}"
        )
else:
    print("Za drogo")