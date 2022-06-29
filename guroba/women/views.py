from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404


# Create your views here.

def women_view(request):
    view = HttpResponse("Страница Women")
    return view

def categories_view(request, catid):
    if int(catid) > 3:
        raise Http404()

    view = HttpResponse(f"<h1> Статьи по категориям </h1> <p>{catid}</p>")
    return view

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1> Страница не найдена </h1>")

def presentHome(request):
    return render(request, 'women/home.html')

def presentAbout(request):
    return render(request, 'women/about.html')