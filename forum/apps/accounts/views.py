from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from .serializers import UserListSerializer, UserStatisticSerializer
from rest_framework import viewsets, generics, mixins, permissions


class SignupView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data

        name = data['name']
        email = data['email']
        password = data['password']

        if User.objects.filter(email=email).exists():
            return Response({'error': 'Email already exists'})
        else:
            if len(password) < 6:
                return Response({'error': 'Password must be at least 6 characters'})
            else:
                user = User.objects.create_user(email=email, password=password, name=name)

                user.save()
                return Response({'success': 'User created successfully'})


class UserListViewSet(viewsets.mixins.ListModelMixin,
                viewsets.GenericViewSet):
    permission_classes = (permissions.AllowAny, )
    queryset = User.objects.all()
    serializer_class = UserListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UserStatisticView(viewsets.mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    permission_classes = (permissions.AllowAny, )
    queryset = User.objects.all()
    serializer_class = UserStatisticSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)