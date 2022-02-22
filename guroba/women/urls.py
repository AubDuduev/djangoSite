from django.urls import path
from women.views import *

urlpatterns = [
    path('', women_view),# пустота это префикс указанный в закометиовонаом women/
    path('categories/', categories_view),
    path('categories/<int:catid>/', categories_view),
    #path('women/', include('women.urls')),#все пути приложения
]