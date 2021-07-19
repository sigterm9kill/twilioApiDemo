#!/usr/bin/env python
# coding: utf-8

# Sean O'Brien
# Twilio API with demo account, the 'to' number is my personal phone, the from is the assigned number from twilio.


from twilio.rest import Client

account_sid = 'AC5dd8e7bed6c2dde07dfcff1c3549a801'
auth_token = 'fbb372f84223ff0dfd28136aedb1979e'
client = Client(account_sid, auth_token)

call = client.calls.create(
    twiml='<Response><Say>Hello Waterfield highering managers, this is a twilio api demonstration from Sean OBrien. Ashley Riedesel from Oak tree Staffing made this happen.</Say></Response>',
    to='+14058940101',
    from_='+14088370516'
)

print(call.sid)


# End.



