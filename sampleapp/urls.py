from django.urls import path
from .views import *


urlpatterns = [
    path('',home,name='index'),
    path('create/',create,name='create'),
    path('details/<int:id>/',details,name='details'),
    path('edit/<int:id>/',edit,name='edit'),
    path('delete/<int:id>/',delete,name='delete'),

    path('article/<int:article_id>/comment/post',comment_post,name='comment_post'),
    path('comment_delete/<int:id>/',comment_delete,name='comment_delete'), 
    path('comment_edit/<int:id>/',comment_edit,name='comment_edit'), 
]
