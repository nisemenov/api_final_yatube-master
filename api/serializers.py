from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Post, Comment, Group, Follow, User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    post = serializers.ReadOnlyField(source='post.id')

    class Meta:
        fields = '__all__'
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('title', 'id')
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
        default=serializers.CurrentUserDefault()
     )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
     )

    def validate(self, data):
        request_user = self.context['request'].user
        following_user = data['following']
        if request_user == following_user:
            raise serializers.ValidationError('You cannot follow yourself!')
        return data

    class Meta:
        fields = ('user', 'following',)
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following',),
            )
        ]
