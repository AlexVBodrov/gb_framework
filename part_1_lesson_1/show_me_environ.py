from wsgiref.simple_server import make_server
from os.path import join
from pprint import pprint


def application(environ, start_response):
    print(type(environ))
    pprint(environ)
    # /part_1_lesson_1/environ.txt
    file_path = join('part_1_lesson_1', 'environ_v2.txt')
    with open(file_path, 'w', encoding='utf-8') as file:
        for k, v in environ.items():
            out_line = f'{k}:{v}\n'
            file.writelines(out_line)
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


with make_server('', 8000, application) as httpd:
    print("Serving on port 8000...")
    httpd.serve_forever()