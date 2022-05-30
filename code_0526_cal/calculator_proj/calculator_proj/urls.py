from django.contrib import admin
from django.urls import path
from calculator_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('result/',result, name="result")
]
