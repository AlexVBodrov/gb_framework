from groot_framework.templator import render

class PageNotFound404:
    def __call__(self, request):
        return '404 WHAT',  render('page_404.html')

