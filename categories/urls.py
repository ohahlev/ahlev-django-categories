from django.conf.urls import url
from . import views

app_name = "categories"
urlpatterns = [
    url('', views.index, name='index'),
]


