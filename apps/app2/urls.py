from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$',views.contextfunc),
    url(r'^logout$',views.logout),
    url(r'^pokes/(?P<id>\d+)/$',views.addpokes),


]
