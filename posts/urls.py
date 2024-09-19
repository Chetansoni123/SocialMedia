from django.urls import path
from posts import views
from users import views as user_views 

from posts.views import (
PostDetailView, PostCreateView, PostUpdateView,
PostDeleteView, showAllUser, UserDetailView)

urlpatterns = [
    path('', views.showPost, name='posts-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('search/', views.search, name='search'),
    path('alluser/', views.showAllUser, name='alluser'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]


