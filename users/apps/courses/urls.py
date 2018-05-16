from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [ 
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^delete/(?P<number>\d+)$', views.delete), 
    url(r'^deletecourse/(?P<number>\d+)$', views.deletecourse),  
]