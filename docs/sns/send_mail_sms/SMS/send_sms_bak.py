#!/usr/bin/env python

"""
import urllib.request
import urllib.parse

def sendSMS(apikey, numbers, sender, message):

    data = urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
                                   'message': message, 'sender': sender})
    data = data.encode('utf-8')
    sms_host_uri = "https://api.textlocal.in/send/?"
    #request = urllib.request.Request("https://api.textlocal.in/send/?")
    request = urllib.request.Request(sms_host_uri)

    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return (fr)


apikey = "K045iCgiC5I-KuGBKySHrWEdO1nDmPRj9CxDaVdtt9"
sender = "PKOTULE"
recipient_to = "7774005057"
message = "Test message from Padmakar using Python"

resp = sendSMS(apikey, recipient_to, sender, message)
print(resp)
"""
import urllib.request
import urllib.parse


def sendSMS(apikey, numbers, sender, message):
    data = urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
                                   'message': message, 'sender': sender})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return (fr)

apikey = "NBc6Q0YC2Ds-9rdxDAKcpXUpuCu10dtMYPmj1Pvn3Z"
resp = sendSMS(apikey, '917774005057', 'TXTLCL', 'Python - This is your message')
print(resp)
