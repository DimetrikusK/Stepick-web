from qa.views import test

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^login/', test),
    url(r'^$', test),
    url(r'^question/', test),
    url(r'^ask/', test),
    url(r'^popular/', test),
    url(r'^new/', test),
    url(r'^signup/', test)
]