from django.conf.urls import url
from . import views

app_name = 'BCrowley_App'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^inspiration', views.inspiration, name='inspiration'),
    url(r'^lists', views.lists, name='lists'),
    url(r'^projects', views.projects, name='projects'),
]
