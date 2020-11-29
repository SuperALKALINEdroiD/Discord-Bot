import twilio
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException


account_file = open("account.txt", "r")
account = account_file.read() 
token_file = open("token.txt", "r")
token = token_file.read()
phone_file = open("phone.txt", "r")
phone = phone_file.read()


account_file.close()
token_file.close()
phone_file.close()

client = Client(account, token)

message = ""


class twilio_message:
    def __init__(self, message_from_discord):
        global message
        message = message_from_discord

    def send_sms(self):
        try:
            global phone
            global message
            message_split = message.split(';')
            send_this = message_split[1]
            client.messages.create(to= phone, from_="+12565738664",  body= send_this )
            return 'Sent!!'
        except TwilioRestException as e:
            return e



tt = twilio_message("twilio;Hello")
print(tt.send_sms())