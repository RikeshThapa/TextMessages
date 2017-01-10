from twilio.rest import TwilioRestClient

account_sid = "AC725f2fc3ac6df495b2a06762cf1918f3"
auth_token = "aeabcc329963ef04a694f43256369c75"
client = TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
    body = "This is Rikesh's new automated texting system",
    to = "xxxxxxxxxx",
    from_ = "xxxxxxxxxx")
print message.sid
