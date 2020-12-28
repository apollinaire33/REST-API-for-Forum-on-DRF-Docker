from django.shortcuts import render
from rest_framework import viewsets, generics, mixins, permissions
from django_filters import rest_framework as filters
from .serializers import PostSerializer, PostDetailSerializer, PostCreateUpdateSerializer, PostLikeDislikeSerializer, CommentListSerializer, CommentCreateUpdateSerializer, CommentLikeDislikeSerializer
from .models import Post, Comment
from .permissions import IsOwner


# post list for all
class PostListView(viewsets.mixins.ListModelMixin,
                viewsets.GenericViewSet):
    permission_classes = (permissions.AllowAny, )
    queryset = Post.objects.filter(is_approved=True)
    serializer_class = PostSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_fields = ('category', )

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# post retrieve for all
class PostRetrieveView(viewsets.mixins.RetrieveModelMixin,
                       viewsets.GenericViewSet):
    permission_classes = (permissions.AllowAny, )
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


# post create by authorized only
class PostCreateView(viewsets.mixins.CreateModelMixin,
                       viewsets.GenericViewSet):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)    
        

# post update and delete by author only
class PostUpdateDeleteView(viewsets.mixins.RetrieveModelMixin,
                        viewsets.mixins.UpdateModelMixin,
                        viewsets.mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    permission_classes = (IsOwner, )
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# post like/dislike by authorized only
class PostLikeDislikeView(viewsets.mixins.RetrieveModelMixin,
                        viewsets.mixins.UpdateModelMixin,
                        viewsets.GenericViewSet):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Post.objects.all()
    serializer_class = PostLikeDislikeSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs) 





# comment list for all
class CommentListView(viewsets.mixins.ListModelMixin,
                viewsets.GenericViewSet):
    permission_classes = (permissions.AllowAny, )
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_fields = ('post', 'author' )

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# commetn create by authorized only
class CommentCreateView(viewsets.mixins.CreateModelMixin,
                       viewsets.GenericViewSet):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Comment.objects.all()
    serializer_class = CommentCreateUpdateSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)    
        

# comment update and delete by author only
class CommentUpdateDeleteView(viewsets.mixins.RetrieveModelMixin,
                        viewsets.mixins.UpdateModelMixin,
                        viewsets.mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    permission_classes = (IsOwner, )
    queryset = Comment.objects.all()
    serializer_class = CommentCreateUpdateSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# comment like/dislike by authorized only
class CommentLikeDislikeView(viewsets.mixins.RetrieveModelMixin,
                        viewsets.mixins.UpdateModelMixin,
                        viewsets.GenericViewSet):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Comment.objects.all()
    serializer_class = CommentLikeDislikeSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs) 