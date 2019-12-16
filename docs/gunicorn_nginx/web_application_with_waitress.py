from wsgiref.simple_server import make_server
from waitress import serve

def application(environ, start_response):
    start_response("200 OK", [("Content-type", "text/plain")])
    return ["Hello my friend!, using waitress WSGI".encode("utf-8")]


serve(application, host='localhost', port=8053)