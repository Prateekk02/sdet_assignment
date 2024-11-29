from django.contrib import admin
from django.urls import path, include
from . import views as v

urlpatterns = [
    path('', v.home, name="home"),
    path('start/', v.start, name = "start"),
    path('stop/', v.stop, name= "stop"),
    path('getUrl/', v.getUrl, name= "getUrl"),
    path('cleanUp/', v.cleanUp, name= "cleanUp")       
]


