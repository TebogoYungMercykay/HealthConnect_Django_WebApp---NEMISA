from django.urls import path
from . import views

urlpatterns = [
    path('all_posts' , views.all_posts, name='all_posts'),
    path('search_posts' , views.search_posts, name='search_posts'),
    path('create_post' , views.create_post, name='create_post'),
    path('get/<int:post_id>' , views.get_post, name='get_post'),
    path('update/<int:post_id>' , views.update_post, name='update_post'),
    path('delete/<int:post_id>' , views.delete_post, name='delete_post'),
    path('create_reply' , views.create_reply, name='create_reply'),
    path('vote' , views.vote, name='vote'),
]
