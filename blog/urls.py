from django.conf.urls import url

from . import views

#装的所有的url
urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^article/(?P<article_id>[0-9]+)$', views.article_page)
]
#要注意是“index/”而不是“index”不然页面会报错