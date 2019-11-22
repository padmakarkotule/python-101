import json
import urllib.request
import urllib.parse


class SendSMS:
    def __init__(self, sender=None, apikey=None):
        # Sender
        # Note: We must get our company name 6 digit as send code from textlocal company.
        # If we don't have our own code then we can use textlocal company code which is TXTLCL
        if sender:
            self.sender = sender
        else:
            self.sender = "TXTLCL"

        # Api key
        # Valid apikey, you can generate apikey from your textlocal account.
        # Login to textlocal -> setting -> API Keys
        if apikey:
            self.apikey = apikey
        else:
            self.apikey = "NBc6Q0YC2Ds-9rdxDAKcpXUpuCu10dtMYPmj1Pvn3Z"

    # def sendSMS(apikey, numbers, sender, message):
    def send_sms(self, recipients, message):

        # SMS service provider uri. E.g. textlocal (https://textlocal.in)
        sms_host_uri = "https://api.textlocal.in/send/?"

        # API key and sender values
        apikey = self.apikey
        sender = self.sender

        # Recipient number (to whom you are sending message)
        recipient_to = recipients

        # Text message
        message = message

        # Prepare data to send message
        data = urllib.parse.urlencode({'apikey': apikey, 'numbers': recipient_to,
                                       'message': message, 'sender': sender})
        data = data.encode('utf-8')
        # Prepare request
        request = urllib.request.Request(sms_host_uri)

        # Set response variable to return response
        rsp = urllib.request.urlopen(request, data)
        rsp_read = rsp.read()
        return (rsp_read)
