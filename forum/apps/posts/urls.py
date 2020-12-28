from django.urls import path
from .views import (PostListView, PostCreateView, PostRetrieveView, PostUpdateDeleteView, PostLikeDislikeView, 
                    CommentListView, CommentCreateView, CommentUpdateDeleteView, CommentLikeDislikeView)
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'', PostListView)
router.register(r'create', PostCreateView)
router.register(r'post', PostRetrieveView)
router.register(r'update', PostUpdateDeleteView)
router.register(r'like_dislike', PostLikeDislikeView)

router.register(r'comments', CommentListView)
router.register(r'comments/create', CommentCreateView)
router.register(r'comments/update', CommentUpdateDeleteView)
router.register(r'comments/like_dislike', CommentLikeDislikeView)

urlpatterns = router.urls