from datetime import date
from views import *


# front controller

# PC
routes = {
    '/': Index(),
    '/about/': About(),
    '/contact/': Contact(),
    '/page/': Page(),
    '/examples/': Examples(),
    '/another_page/': AnotherPage(),
}
