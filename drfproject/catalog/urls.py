from django.conf.urls import url, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_jwt.views import refresh_jwt_token

urlpatterns = [
    url(r'^products/$', views.ProductList.as_view(), name='product-list'),
    url(r'^products/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view()),
    url(r'^products/(?P<product_id>[0-9]+)/reviews/$', views.ReviewList.as_view()),
    url(r'^products/(?P<product_id>[0-9]+)/reviews/(?P<review_id>[0-9]+)/$',
        views.ReviewDetail.as_view()),
    url(r'^products2/$', views.ProductList2.as_view()),
    url(r'^', include('rest_auth.urls')),
    url(r'^registration/', include('rest_auth.registration.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest_auth/registration/', include('rest_auth.registration.urls')),
    url(r'^refresh-token/', refresh_jwt_token),
]
