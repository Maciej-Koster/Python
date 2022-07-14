import requests
from datetime import datetime
import smtplib
import keys

MY_LAT = -35.064651 # Your latitude
MY_LONG = 151.944981 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
dane = response.json()


def check_if_its_near():
    iss_latitude = float(dane["iss_position"]["latitude"])
    iss_longitude = float(dane["iss_position"]["longitude"])
    if (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5):
        if (MY_LONG - 5) <= iss_longitude <= (MY_LONG + 5):
            return True
    else:
        return False


#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
godzina = time_now.hour

check_if_dark = False
if sunset < godzina <= 24 or 0 <= godzina <= sunrise:
    check_if_dark = True

my_email = keys.test_email_1
password = keys.password_test_email_1

check = check_if_its_near()

if check_if_dark is True and check is True:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=keys.my_email_gmail,
            msg="Subject: Hello\n\nsatelita kolo ciebie!!!"
        )
    print("wadomośc wysłana")


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



