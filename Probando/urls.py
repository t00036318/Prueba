from django.conf.urls import url
# from django.core.urlresolvers import reverse
from . import views

urlpatterns = [
    url(r'^$', views.RequestsHandler, name="RequestsHandler"),

]
