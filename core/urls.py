from django.conf.urls import url

from . import views

app_name = 'core'
urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^home/$', views.signup, name='home'),
    url(r'^login/$', views.signup, name='login'),
    url(r'^logout/$', views.signup, name='logout')
]