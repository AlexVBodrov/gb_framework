from wsgiref.simple_server import make_server


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'Hello world from a simple WSGI application! version 2.0']


with make_server('', 8080, application) as httpd:
    print("Serving on port 8080...")
    httpd.serve_forever()