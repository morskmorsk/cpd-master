# from rest_framework import generics
# from .models import CustomUser
# from .serializers import CustomUserSerializer


# class UserListCreateAPIView(generics.ListCreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer


# class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework import viewsets


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer