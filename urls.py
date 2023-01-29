from datetime import date
from views import *


# front controller

# PC
routes = {
    '/': Index(),
    '/index/': Index(),
    '/#/': Index(),
    '/about/': About(),
    '/contact/': Contact(),
    '/page/': Page(),
    '/examples/': Examples(),
    '/another_page/': AnotherPage(),
}
