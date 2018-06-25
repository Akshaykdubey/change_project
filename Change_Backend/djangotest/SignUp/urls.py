from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index, name= 'SignUp'),
    url(r'^register$', views.userFormview, name='Register'),
]
