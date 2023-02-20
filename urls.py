from datetime import date
from views import Index


# front controller
def secret_front(request):
    request['date'] = date.today()


def other_front(request):
    request['key'] = 'key'


fronts = [secret_front, other_front]

# PC
# routes = {
#     '/': Index(),
#     '/index/': Index(),
#     '/#/': Index(),
#     '/about/': About(),
#     '/contact/': Contact(),
#     '/study_programs/': StudyPrograms(),
#     '/courses-list/': CoursesList(),
#     '/create-course/': CreateCourse(),
#     '/create-category/': CreateCategory(),
#     '/category-list/': CategoryList(),
#     '/copy-course/': CopyCourse()
# }
