from django.urls import path
from . import api_views as views

urlpatterns = [
    path('users/', views.UserListCreateAPIView.as_view(),
         name='user_list_create'),
    path('users/<int:pk>/', views.UserRetrieveUpdateDestroyAPIView.as_view(),
         name='user_retrieve_update_destroy'),
]
