from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path(r'^post/(?P<pk>\d+)/', views.post_detail, name='post_detail'),
    path(r'^post/new/', views.post_new, name='post_new'),
    path(r'^post/(?P<pk>\d+)/edit/', views.post_edit, name='post_edit'),
    path(r'^drafts/', views.post_draft_list, name='post_draft_list'),
    path(r'^post/(?P<pk>\d+)/publish/', views.post_publish, name='post_publish'),
    path(r'^post/(?P<pk>\d+)/remove/', views.post_remove, name='post_remove'),
    path(r'^accounts/login/$', views.signin, name='login'),
    path(r'^accounts/logout/$', views.sign_out, name='logout'),
    path(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    path(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    path(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    path(r'^accounts/signup/$', views.signup, name='signup'),
    path(r'^space/', views.space, name='space'),
    path(r'^space2/', views.space2, name='space2'),
    path(r'^space3/', views.space3, name='space3'),
    path(r'^space4/', views.space4, name='space4'),
    path(r'^space5/', views.space5, name='space5'),
    path(r'^space6/', views.space6, name='space6'),
    #, kwargs={'next_page': '/'}

]