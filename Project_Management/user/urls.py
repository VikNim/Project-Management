from django.conf.urls import url
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'user/Login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/user/login'}, name='logout'),
    url(r'^register/', RegisterView.as_view(), name='register'),
    # url(r'^profile/', )
]
