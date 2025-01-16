from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostListView.as_view(), name='forum-home'),
    path('contact/', views.ContactUsView.as_view(), name='contact-us'),
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post-detail'),
    path('<slug:slug>/comments/', views.PostCommentsView.as_view(), name='post-comments'),
]