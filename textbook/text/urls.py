from importlib.resources import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('s1', views.s1, name='s1'),
    path('s2', views.s2, name='s2'),
    path('s3', views.s3, name='s3'),
    path('s4', views.s4, name='s4'),
    path('s4_1', views.s4_1, name='s4_1'),

]
