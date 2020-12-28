from rest_framework import serializers
from django.contrib.auth import get_user_model
from posts.serializers import PostByUserSerializer, CommentByUserSerializer
User = get_user_model()


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'name')


class UserStatisticSerializer(serializers.ModelSerializer):
    posts_by_author = serializers.SerializerMethodField()
    comments_by_author = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'posts_by_author', 'comments_by_author')

    def get_posts_by_author(self, instance):
        posts_by_author = instance.posts_by_author.order_by('id')
        return PostByUserSerializer(posts_by_author, many=True).data

    def get_comments_by_author(self, instance):
        comments_by_author = instance.comments_by_author.order_by('id')
        return CommentByUserSerializer(comments_by_author, many=True).data