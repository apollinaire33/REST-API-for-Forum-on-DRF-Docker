from rest_framework import serializers
from .models import Post, Comment

# serializers for posts
class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'category', 'pub_date', 'likes', 'dislikes')


class PostDetailSerializer(serializers.ModelSerializer):
    comments_to_post = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'category', 'pub_date', 'likes', 'dislikes', 'text', 'comments_to_post')

    def get_comments_to_post(self, instance):
        comments_to_post = instance.comments_to_post.order_by('id')
        return CommentListSerializer(comments_to_post, many=True).data


class PostCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'category', 'text')


class PostLikeDislikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'likes', 'dislikes')


class PostByUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('title', 'likes', 'dislikes')



# serializers for comments
class CommentListSerializer(serializers.ModelSerializer):
    post = serializers.CharField(source="post.title")

    class Meta:
        model = Comment
        fields = ('id', 'post', 'author', 'text', 'created_on', 'likes', 'dislikes', 'reply')


class CommentCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'post', 'author', 'text', 'reply')


class CommentLikeDislikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'likes', 'dislikes')


class CommentByUserSerializer(serializers.ModelSerializer):
    post = serializers.CharField(source="post.title")

    class Meta:
        model = Comment
        fields = ('post', 'text', 'likes', 'dislikes')

