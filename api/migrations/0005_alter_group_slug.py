# Generated by Django 4.2.3 on 2023-08-04 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_author_follow_following_alter_comment_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=models.SlugField(blank=True, null=True, verbose_name='Slug'),
        ),
    ]
