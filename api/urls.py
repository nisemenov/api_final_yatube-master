from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import (
    PostViewSet,
    CommentViewSet,
    GroupViewSet,
    FollowViewSet,
)


router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'posts/(?P<post_id>[^/.]+)/comments', CommentViewSet,
                basename='comments')
router.register(r'group', GroupViewSet)
router.register(r'follow', FollowViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
