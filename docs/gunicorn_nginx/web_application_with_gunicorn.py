from wsgiref.simple_server import make_server

def application(environ, start_response):
    start_response("200 OK", [("Content-type", "text/plain")])
    return ["Hello my friend!, using Gunicorn WSGI".encode("utf-8")]


#server = make_server('localhost', 8051, application)
#server.serve_forever()