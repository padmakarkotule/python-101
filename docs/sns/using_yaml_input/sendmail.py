#!/usr/bin/env python
import pika
import json
import smtplib
import threading
import string
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import jinja2

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',
                         exchange_type='topic')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

# binding_keys = sys.argv[1:]
# if not binding_keys:
#     sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
#     sys.exit(1)

# for binding_key in binding_keys:
channel.queue_bind(exchange='topic_logs',
                   queue=queue_name,
                   routing_key='email.*')

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))
    my_json = body.decode('utf8').replace("'", '"')
    request_data = json.loads(my_json)
    print(request_data['subject'])
    print("data is in on way")

    # mail configurations
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("djangomailhost@gmail.com", "restdjango")
    me = "djangomailhost@gmail.com"
    you = "chokhareganesh@gmail.com"  # request_data['recepientMail']

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Approval for New Resources"
    msg['From'] = me
    msg['To'] = you
    msg['CC'] = me
    msg['BCC'] = me

    # Create the body of the message (a plain-text and an HTML version).
    text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttps://www.python.org"

    # importing template and add your own parmeter to render {{}}
    with open("./test.html", "r") as myfile:
        html_content = myfile.read()  # removed `replace` to preserve newline
    formatted = jinja2.Template(html_content).render(name="ganeshssss")

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(formatted, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    server.sendmail("djangomailhost@gmail.com", you, msg.as_string())
    server.quit()


channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()