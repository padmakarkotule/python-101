# web_application-1.py
import json
from wsgiref.simple_server import make_server

def application(environ, start_response):
    path = environ.get('PATH_INFO')
    if path == '/':
        response_body = "Index"
    else:
        response_body = "Hello"
    status = "200 OK"
    #response_headers = [("Content-Length", str(len(response_body)))]
    response_headers = [("Content-Type", "8")]
    start_response(status, response_headers)

    return [response_body]


# def app(environ, start_response):
#     # pass
#     path = environ.get('PATH_INFO')
#     if path == '/':
#         response_body = "Index"
#     else:
#         response_body = "Hello"
#     status = "200 OK"
#     response_headers = [("Content-Length", str(response_body))]
#     start_response(status, response_headers)
#
#     return response_headers

httpd = make_server('127.0.0.1', 8051, application)
httpd.serve_forever()
