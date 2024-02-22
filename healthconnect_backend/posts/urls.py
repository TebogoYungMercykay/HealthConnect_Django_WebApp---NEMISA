from django.urls import path
from . import views

urlpatterns = [
    path('all_posts' , views.all_posts, name='all_posts'),
    path('articles', views.articles , name='articles'),
    path('search_posts' , views.search_posts, name='search_posts'),
    path('create_post' , views.create_post, name='create_post'),
    path('get/<int:post_id>/<str:fragment>/' , views.get_post_reply, name='get_post_reply'),
    path('get/<int:post_id>' , views.get_post, name='get_post'),
    path('update/<int:post_id>' , views.update_post, name='update_post'),
    path('delete/<int:post_id>' , views.delete_post, name='delete_post'),
    path('create_reply' , views.create_reply, name='create_reply'),
    path('react_to_post/<int:post_id>' , views.react_to_post, name='react_to_post'),
]
