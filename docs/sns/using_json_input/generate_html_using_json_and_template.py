#!/usr/bin/python
#import jinja2, yaml
#from pathlib import Path
import jinja2, json
# libraries to be imported to send mail
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def generate_email_output(template_file_name, payload):
    # Declare email template file path.
    templateFilePath = jinja2.FileSystemLoader('./templates/')

    # Set Jinja2 environment
    jinja2_env = jinja2.Environment(loader=templateFilePath)

    # Provide Email html template file.
    jinja_template = jinja2_env.get_template(template_file_name)

    #template_input = payload

    # Provide email output path. e.g. signup.html
    email_html_output_file = "signup_using_json.html"

    #with open(template_input_file) as file:
    input_data = payload
    output = jinja_template.render(input_data)
    #print("Output:", output)
    #print(output)


    with open(email_html_output_file, 'w') as output_file:
        output_file.write(output)


def send_email():
    title = "Development App"
    logo_image = "img/byjus.jpg alt=\"Logo\" width=\"350\" height=\"90\""
    parent_name = "Padmakar"
    child_name = "Pranav Kotule"
    phone_number = "+91-7774005057"
    paragraph_1 = """
    Test data <br>
    Test data <br>
    Test data <br>
    """

    data = {'title': title , 'parent_name': parent_name, 'child_name': child_name, 'logo_image': logo_image, 'phone_number': phone_number}
    generate_email_output("email_html_template.j2", data)

    # mail configurations
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("djangomailhost@gmail.com", "restdjango")
    me = "djangomailhost@gmail.com"
    you = "padmakar.kotule@gslab.com"  # request_data['recepientMail']

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Test mail using Python"
    msg['From'] = me
    msg['To'] = you
    msg['CC'] = me
    msg['BCC'] = me

    # open the file to be sent
    filename = "signup_using_json.html"
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

    server.sendmail("djangomailhost@gmail.com", you, msg.as_string())
    server.quit()

# Send mail
send_email()
