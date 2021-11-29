from django.http import HttpResponse


def index(request):
    return HttpResponse('главная')


def group_posts(request, slug):
    return HttpResponse('Группы')
