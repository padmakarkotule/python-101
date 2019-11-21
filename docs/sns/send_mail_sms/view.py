from signup_email import send_email


# Send email

parent_name = "Padmakar Kotule"
child_name = "Pranav Kotule"
recipient_to = ['padmakar.kotule@gslab.com']
recipient_cc = ['padmakar.kotule@gslab.com']
recipient_bcc = ['padmakar.kotule@gslab.com']
subject = "Welcome to <gsl> - Test Mail"

data = {'parent_name': parent_name,
        'child_name': child_name,
        'recipient_to': recipient_to,
        'recipient_cc': recipient_cc,
        'recipient_bcc': recipient_bcc,
        'subject': subject
        }

mail = send_email()
#mail.generate_html_output(data)
mail.send_mail(data)