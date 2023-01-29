from wsgiref.simple_server import make_server

from groot_framework.main import Framework
from urls import routes


application = Framework(routes)

PORT_NUM = 8080

with make_server('', PORT_NUM, application) as httpd:
    print(f"Запуск на порту {PORT_NUM}...")
    httpd.serve_forever()
