from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="posts")
    group = models.ForeignKey('Group', on_delete=models.CASCADE,
                              blank=True, null=True,
                              related_name='posts',
                              verbose_name='группа')

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    text = models.TextField()
    created = models.DateTimeField('Date of create',
                                   auto_now_add=True, db_index=True)


class Group(models.Model):
    title = models.CharField('Title', max_length=200)
    slug = models.SlugField('Slug', blank=True, null=True)
    description = models.TextField('Description', blank=True, null=True)

    def __str__(self):
        return self.title


class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='follower')
    following = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name='following')

    class Meta:
        unique_together = ['user', 'following']
