from django.contrib import admin
from django.conf.urls import url

from mainapp import views

urlpatterns = [
    url(r'^$', views.homepage, name='home'),
    url(r'^admin/', admin.site.urls),
]
