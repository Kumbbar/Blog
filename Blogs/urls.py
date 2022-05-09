from django.urls import path
from . import views

app_name = 'Blogs'

urlpatterns = [
    path('', views.index, name='index'),
    path('new_blog/', views.new_blog, name='new_blog'),
    path('edit_blog/<int:blog_id>/', views.edit_blog, name='edit_blog'),
    path('edit_allblogs', views.edit_all_blogs, name='edit_all_blogs')
]