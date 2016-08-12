from django.conf.urls import url
from django.contrib import admin
from posts import views as posts_views

urlpatterns = [
    url(r'^$', posts_views.post_list, name='List Post'),
    url(r'^create/$', posts_views.post_create, name='Create Post'),
    url(r'^detail/(?P<id>\d+)/$', posts_views.post_detail, name='detail'),
    url(r'^update/$', posts_views.post_update, name='Update Post'),
    url(r'^delete/$', posts_views.post_delete, name='Delete Post'),
]
