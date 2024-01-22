from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, permissions
from .models import Post, Group, Follow, User
from api.serializers import (PostSerializer,
                             CommentSerializer,
                             GroupSerializer,
                             FollowSerializer)
from .permissions import IsOwnerObj
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerObj,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('group',)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=False)
    def count(self, request):
        count = Post.objects.count()
        return Response({"count": count})


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerObj,)

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    filterset_fields = ('user__username',)
    search_fields = ('=user__username', '=following__username',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.query_params.get('user', None)
        if user is not None:
            return Follow.objects.filter(user__username=user)
        return Follow.objects.all()
