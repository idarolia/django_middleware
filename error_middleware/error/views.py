from django.http import HttpResponse


def index(request):
    text = '<h2> This is error app homepage</h2>'
    return HttpResponse(text)

