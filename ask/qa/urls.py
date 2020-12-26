from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^login/', views.test),
    url(r'^$', views.test),
    url(r'^question/', views.test),
    url(r'^ask/', views.test),
    url(r'^popular/', views.test),
    url(r'^new/', views.test),
    url(r'^signup/', views.test)
]