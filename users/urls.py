from .api_views import CustomUserViewSet
from rest_framework import routers
from django.urls import include, path
from .views import (CustomUserListView, CustomUserDetailView,
                    CustomUserCreateView, CustomUserUpdateView,
                    CustomUserDeleteView)

router = routers.DefaultRouter()

router.register(r'users', CustomUserViewSet)


urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework_home')),
    path('', CustomUserListView.as_view(),
         name='users_list'),
    path('users_detail/<int:pk>/', CustomUserDetailView.as_view(),
         name='users_detail'),
    path('users_create/', CustomUserCreateView.as_view(),
         name='users_create'),
    path('users_update/<int:pk>/', CustomUserUpdateView.as_view(),
         name='users_update'),
    path('users_delete/<int:pk>/', CustomUserDeleteView.as_view(),
         name='users_delete'),
]
