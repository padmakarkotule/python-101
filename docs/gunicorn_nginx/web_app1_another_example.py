from wsgiref.simple_server import make_server

def application(environ, start_response):
    start_response("200 OK", [("Content-type", "text/plain")])

    fh = open("ulysses.txt")
    lines = [fh.readline().encode("utf-8") for i in range(30)]

    return lines


server = make_server('localhost', 8052, application)
server.serve_forever()