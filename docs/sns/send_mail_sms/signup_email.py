#!/usr/bin/python
import jinja2, json, yaml
from pathlib import Path

# send mail libraries to be imported
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.header import Header, decode_header, make_header
from email.utils import COMMASPACE, formatdate


class send_email:
    def __init__(self):
        self.smtp_server = "smtp.gmail.com"

    def generate_html_output(self, email_data):
        # Get data to generate html page.

        #title = email_data['title']
        #logo_image = email_data['logo_image']
        parent_name = email_data['parent_name']
        child_name = email_data['child_name']
        #phone_number = email_data['phone_number']
        #message = email_data['message']

        payload = {'parent_name': parent_name, 'child_name': child_name}

        # Declare email template file path.
        templateFilePath = jinja2.FileSystemLoader('./templates/')

        # Set Jinja2 environment
        jinja2_env = jinja2.Environment(loader=templateFilePath)

        # Template file name
        template_file_name = "signup_html_template.j2"
        # Provide Email html template file.
        jinja_template = jinja2_env.get_template(template_file_name)

        #template_input = payload

        # Provide email output path. e.g. signup.html
        html_output_file = "signup.html"

        #with open(template_input_file) as file:
        input_data = payload
        output = jinja_template.render(input_data)
        #print("Output:", output)
        #print(output)

        with open(html_output_file, 'w') as output_file:
            output_file.write(output)

    #def send(subject, recipient_list = [], text, html = None, files = [], replyto = None):
    def send_mail(self, email_data):

    #def send(self, subject, recipient_list=[], text, html=None, files=[], replyto=None):
        # In future ref. link to explore more things.
        # https://denis.papathanasiou.org/archive/2010.09.04.post.pdf

        # smtp/email configuration
        email_smtp_config_file = "files/email_smtp_config.yml"
        with open(email_smtp_config_file) as file:
            input_data = yaml.load(file, Loader=yaml.FullLoader)

        # Convert yml data into json object.
        # Note:- input_data is already dict object, so no need to use json dumps again.
        #json_output = json.dumps(input_data, indent=4, separators=(',', ': '))

        # Load SMTP config data.
        #  server = smtplib.SMTP('smtp.gmail.com', 587)
        #smtp_server = json_output['smtp_server']
        smtp_server = input_data['smtp_server']
        smtp_port_tls = input_data['smtp_port_tls']
        email_service_account = input_data['email_service_account']
        email_service_account_password = input_data['email_service_account_password']
        server = smtplib.SMTP(smtp_server, smtp_port_tls)
        server.starttls()
        #server.login("djangomailhost@gmail.com", "restdjango")
        server.login(email_service_account, email_service_account_password)

        # Load email config data e.g. sender, recipient_list=[], etc.
        #me = "djangomailhost@gmail.com"
        sender = email_service_account
        #you = "padmakar.kotule@gslab.com"  # request_data['recepientMail']
        recipient_to = email_data['recipient_to']
        recipient_cc = email_data['recipient_to']
        recipient_bcc = email_data['recipient_to']
        subject = email_data['subject']

        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        # msg['Subject'] = "Test mail using Python"
        msg['Subject'] = subject
        # msg['From'] = me
        # msg['From'] = recipient_to
        msg['From'] = email_service_account
        # msg['To'] = you
        # msg['CC'] = me
        # msg['BCC'] = me
        msg['To'] = recipient_to
        msg['CC'] = recipient_cc
        msg['BCC'] = recipient_bcc

        # open the file to be sent
        filename = "signup.html"
        attachment = open(filename, "rb")
        # instance of MIMEBase and named as p
        p = MIMEBase('application', 'octet-stream')
        # To change the payload into encoded form
        p.set_payload((attachment).read())
        # encode into base64
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        # attach the instance 'p' to instance 'msg'
        msg.attach(p)

        #msg.attach(part1)
        #msg.attach(part2)

        #server.sendmail("djangomailhost@gmail.com", you, msg.as_string())
        server.sendmail(sender, recipient_to, recipient_cc, msg.as_string())
        server.quit()

    # Send mail
    #send_email()
