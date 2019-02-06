from django.conf.urls import url, include
from django.views.generic.base import RedirectView

app_name = "marketupdate_frontend"
# Redirect any request that goes into here to static/index.html
urlpatterns = [
    url(r'^$', RedirectView.as_view(url='static/index.html', permanent=False), name='index'),
    url(r'^favicon.ico', RedirectView.as_view(url='static/favicon.ico', permanent=False), name='favicon'),
]