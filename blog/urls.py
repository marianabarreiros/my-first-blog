from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
    #adicionei o 'name='post-detail' na primeira url pois, quando eu tentava adicionar uma postagem nova dava erro: Reverse for 'post_detail' with arguments '()' and keyword arguments '{'pk': 13}' not found. 0 pattern(s) tried: []
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]