from twilio.rest import TwilioRestClient
account = "xxxxxx"
token = "xxxxxxxxxxx"
client = TwilioRestClient(account, token)

message = client.sms.messages.create(to="+8618605206605",
                                     from_="+12342004043",
                                     body="Hello there!")