from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostListView.as_view(), name='forum-home'),
    path('contact/', views.ContactUsView.as_view(), name='contact-us'),
]