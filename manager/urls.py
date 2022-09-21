from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('manager/', admin.site.urls),
]
