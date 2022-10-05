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
    path('s4_2', views.s4_2, name='s4_2'),
    path('s4_3', views.s4_3, name='s4_3'),
    path('s4_4', views.s4_4, name='s4_4'),
    path('s4_5', views.s4_5, name='s4_5'),
    path('s4_6', views.s4_6, name='s4_6'),
    path('s4_7', views.s4_7, name='s4_7'),
    path('s4_8', views.s4_8, name='s4_8'),
    path('s4_9', views.s4_9, name='s4_9'),
    path('s5', views.s5,name = 's5'),
    path('s6',views.s6,name='s6'),
    path('s7',views.s7,name='s7'),

]
