from django.conf.urls import url, include
from django.contrib import admin
from .views import IndexView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='Home'),
    url(r'^home/', IndexView.as_view(), name='Home'),
    url(r'^user/', include('user.urls', namespace='user')),
]
