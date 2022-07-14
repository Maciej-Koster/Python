from twilio.rest import Client
import smtplib
import keys

TWILIO_SID = keys.twilio_account_sid
TWILIO_AUTH_TOKEN = keys.twilio_auth_token
TWILIO_VIRTUAL_NUMBER = keys.twilio_number
TWILIO_VERIFIED_NUMBER = keys.my_number
MY_EMAIL = keys.test_email_1
PASSWORD = keys.password_test_email_1

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER
            )
        print(message.sid)

    def send_email(self, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()  # włączenie zabezpieczenia, standard tls
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=keys.my_email_gmail, ## ADRES EMAIL Z ARKUSZA !!!!!!!!!!!!!!!!!1
                msg=f"Subject: Hello\n\n{message}"
            )