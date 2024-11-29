from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', admin.site.urls, include('control_browser.urls')),
       
]
