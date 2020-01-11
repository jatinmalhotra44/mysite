from django.urls import path
from basicapp import views
from django.conf.urls import url
urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.reg,name='register'),
]
