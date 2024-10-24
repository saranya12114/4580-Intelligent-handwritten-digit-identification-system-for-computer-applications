from . import views
from django.urls import path

urlpatterns=[
    path("",views.index,name='index'),
    path("about", views.about, name='about'),
    path("upload",views.upload,name='upload'),
    path("result", views.upload,name='result')
]