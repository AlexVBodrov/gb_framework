
from groot_framework.requests import PostRequests, GetRequests
from groot_framework.page_404 import PageNotFound404


class Framework:

    """Класс Framework - основа WSGI-фреймворка"""

    def __init__(self, routes_obj, fronts_obj=None):
        self.routes_lst = routes_obj
        self.fronts_obj = fronts_obj

    def __call__(self, environ, start_response):
        # Получаем адрес, по которому пользователь выполнил переход
        path = environ['PATH_INFO']
        
        #убираем из путей .html
        if path.endswith('.html'):
            path = path.replace('.html', '')


        # Добавляем закрывающий слеш
        if not path.endswith('/'):
            path = f'{path}/'

        request = {}
        # Получаем все данные запроса
        method = environ['REQUEST_METHOD']
        request['method'] = method

        if method == 'POST':
            data = PostRequests().get_request_params(environ)
            request['data'] = data
            print(f'Нам пришёл post-запрос: {PostRequests.decode_value(data)}')
        if method == 'GET':
            request_params = GetRequests().get_request_params(environ)
            request['request_params'] = request_params
            print(f'Нам пришли GET-параметры: {request_params}')

        # Находим нужный контроллер
        if path in self.routes_lst:
            view = self.routes_lst[path]
        else:
            view = PageNotFound404()

        # Запускаем контроллер
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]
