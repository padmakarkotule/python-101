from wsgiref.simple_server import make_server

def application(environ, start_response):
    start_response("200 OK", [("Content-type", "text/plain")])
    return ["Hello my friend! Webapp (This app) with uWSGI".encode("utf-8")]

