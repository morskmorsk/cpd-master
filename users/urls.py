# from django.urls import path
# from . import api_views as views

# urlpatterns = [
#     path('users/', views.UserListCreateAPIView.as_view(),
#          name='user_list_create'),
#     path('users/<int:pk>/', views.UserRetrieveUpdateDestroyAPIView.as_view(),
#          name='user_retrieve_update_destroy'),
# ]
from .api_views import CustomUserViewSet
from rest_framework import routers
from django.urls import include, path

router = routers.DefaultRouter()

router.register(r'users', CustomUserViewSet)


urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework_home')),
]
