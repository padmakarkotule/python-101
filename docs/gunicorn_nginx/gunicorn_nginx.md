# Basic of Web Server Gateway Interface 
(Before using Gunicorn, or uWSGI, or waitress with Nginx / apache. )
Ref. Link - https://www.agiliq.com/blog/2013/07/basics-wsgi/
### Web Server
Web Server: When we say web server, we mean the software, and not the machine that stores your code. 
This server recieves the request from a client(Web browser) and returns a response. 
**Web server doesn’t create the response, it only returns the response.** So, a server needs to talk 
with a **Web Application which can create a response.**

### Web Application
Web Application: Web Server will get the response from it. It is the job of the Web Application to 
create a response based on the url and pass this response back to the Web Server. 
Web Server’s job is only to return this response to the client.

### WSGI
WSGI: WSGI is an interface. **It is just a specification or a set of rules. WSGI is not a software. 
WSGI is not a library or a framework.** *WSGI is not something you can install via pip.*

WSGI comes into picture because the Web Server needs to communicate with the Web Application. 
WSGI specifies the rules which needs to be implemented by the Web Application side and the Web Server side
so that they can interact with each other. So, 
**a WSGI compliant server will be able to communicate with a WSGI compliant Web Application.**
For example,
In WSGI architecture, **WSGI Application has to be a callable and it needs to be given to the Web Server, 
so the Web Server can call the Web Application whenever the server recieves a request.**
Please see following high level architectural diagram which shows communication between
Client<--->webserver<--->WSGI<--->WebAppFramwork_Example_Python_Django 


For more understanding why WSGI came into existence, read about WSGI on wikipedia.
[WSGI wikipedia](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface)

###### Example (Writing our Web Application)
    `
    #web_application.py
    from wsgiref.simple_server import make_server
    
    def application(environ, start_response):
        start_response("200 OK", [("Content-type", "text/plain")])
        return ["Hello my friend!".encode("utf-8")]

    server = make_server('localhost', 8051, application)
    server.serve_forever()     
    `
Run this file "python web_application.py". Visit http://127.0.0.1:8051/  
You will see page with response Hello my friend!.


Stepping through the code.

- Python provides a function called `make_server`. We can use this function to create 
  a WSGI compliant server provided by Python.
- We created a callable called application. You can think of this callable as Web Application.
- `make_server()` creates an instance of WSGI compliant server. So, httpd is the Web Server in our case.
- The first and second argument to make_server specifies the host and port on which the server will 
  listen for requests.
- Third argument to make_server passes the Web Application which the Web Server would use to get the response.
- In the last line we start the web server using serve_forever.

**IMP**
- The function "application" - used as the third parameter of make_server - It needs two parameters:
    - environ
    - start_response: 
        - start_response has to be a callable with three parameters: 
            - status, response_headers, exc_info=None
                - status contains the numeric HTTP status code of the response, 
                  - e.g. "200 OK", "404 NOT FOUND", or "500 SERVER ERROR". 
                - response_headers contains the HTTP message for the status code used. 
                - exc_info used for traceback information is optional.
 
Whenever a request comes, Web Server running on port 8051 will call the Web Application which in our 
case is the callable application. <br>

Another example,
Ref. Link - https://www.python-course.eu/dynamic_websites_wsgi.php

    `
        from wsgiref.simple_server import make_server
        
        def application(environ, start_response):
            start_response("200 OK", [("Content-type", "text/plain")])
        
            fh = open("ulysses.txt")
            lines = [fh.readline().encode("utf-8") for i in range(30)]
        
            return lines
        
        
        server = make_server('saturn', 8080, application)
        server.serve_forever()
    `

**Note** Sample code shown in above exaple is not used from site - https://www.agiliq.com/blog/2013/07/basics-wsgi/<br>
         because it was getting some issue e.g.  "write() argument must be a bytes instance"<br>
         Instead of that example, I have refered link https://www.python-course.eu/dynamic_websites_wsgi.php<br>
         and taken Simple Example with WSGI.<br>


#### Gunicorn - Let’s run our web application with gunicorn instead of make_server.

**Note** - Gunicorn doesn't support windows, for windows use alternative WSGI e.g. waitress

Copy web_application.py to web_application_with_gunicorn.py and comment the lines 
which correspond to make_server. So comment these two lines.

    server = make_server('localhost', 8051, application)
    server.serve_forever()

- Install gnicorn
    `pip install gunicorn`
`
    from wsgiref.simple_server import make_server

    def application(environ, start_response):
        start_response("200 OK", [("Content-type", "text/plain")])
        return ["Hello my friend!, using Gunicorn WSGI".encode("utf-8")]
     
     
    `#server = make_server('localhost', 8051, application)`
    
    `#server.serve_forever()`
`
- Run your web application with gunicorn, e.g.
    `gunicorn web_application:application --bind=localhost:8051`

 
#### Waitress - Gunicorn not supported on Windows, alternative is use waitress
Ref. Links
https://stackoverflow.com/questions/11087682/does-gunicorn-run-on-windows
https://docs.gunicorn.org/en/stable/index.html
    (As per this link gunicorn is WSGI HTTP server for UNIX).

**Gunicorn does not support Windows, it is  for UNIX** to work with the application <br>
Refer the below link for more details,<br>
https://github.com/benoitc/gunicorn/issues/524 <br>

**Alternative of Gunicorn on Windows** 
So What’s the alternative of  Gunicorn on windows. 
alternative of Gunicorn on windows is the `Waitress`.

**Setup:**
    `$ pip install waitress`
 
**Sample code**
`
    from wsgiref.simple_server import make_server
    from waitress import serve

    def application(environ, start_response):
        start_response("200 OK", [("Content-type", "text/plain")])
        return ["Hello my friend!, using waitress WSGI".encode("utf-8")]

    serve(application, host='localhost', port=8053)
`

So it was very easy to switch from one wsgi compliant web server, i.e make_server, 
to another wsgi compliant web server, i.e gunicorn.


####uWSGI - another wsgi compliant web server

- Install uwsgi
    `pip install uwsgi`
- Use uwsgi to serve your web application.
    `uwsgi --http :8051 --wsgi-file web_application.py`
- You should be able to access http://localhost:8051/.
**Note**
There is no support for windows, but you can use uWSGI in the linux subsystem in windows 10.
Ref. - https://github.com/unbit/uwsgi/issues/1930



# Setting up Django with Nginx, Gunicorn
