from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^products/$', views.ProductList.as_view()),
    url(r'^products2/$', views.ProductList2.as_view()),
]
