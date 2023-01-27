from wsgiref.simple_server import make_server


def application(environ, start_response):
    print(type(environ))
    print(environ)
    with open('environ.txt', 'w', encoding='utf-8') as file:
        file.write(str(environ))
    path = environ['PATH_INFO']
    if path == '/':
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [b'Index']
    elif path == '/abc/':
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [b'ABC']
    else:
        start_response('404 NOT FOUND', [('Content-Type', 'text/html')])
        return [b'404 Not Found']


with make_server('', 8080, application) as httpd:
    print("Serving on port 8080...")
    httpd.serve_forever()