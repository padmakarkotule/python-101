import json
from send_sms import SendSMS


def send_sms_normal_msg(recipient, message):

    # sms request paramenter. - sender and apikey,
    # else it will use default set in backend code.
    sms = SendSMS(sender=None, apikey=None)

    # Send sms
    # Enter recipient phone number to whom you want to send sms e.g. 7774005057
    recipient_to = recipient

    # Enter your message
    message = message

    # sms response
    sms_rsp = sms.send_sms(recipient_to, message)


def send_sms_activate_account(recipient):

    # sms request paramenter. - sender and apikey,
    # else it will use default set in backend code.
    sms = SendSMS(sender=None, apikey=None)

    # Send sms
    # Enter recipient phone number to whom you want to send sms e.g. 7774005057
    recipient_to = recipient

    # Enter your message
    otp = getotp()
    message = "Test Msg. Dear customer," + otp + "is OTP to activate your CLICK account. OTP are SECRET.DO not disclose it to anyone"
    # sms response
    sms_rsp = sms.send_sms(recipient_to, message)

    #resp = sendSMS(apikey, recipient_to, sender, message)
    print("API Key Response\n", type(sms_rsp))
    print("\n", sms_rsp)


def getotp():
    # Generate otp and send it.
    otp = "223456"
    return otp


# Recipient phone number
recipient_number = '7774005058'
send_sms_activate_account(recipient_number)