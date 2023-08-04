# Generated by Django 4.2.3 on 2023-08-03 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_post_group'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='author',
            new_name='following',
        ),
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Date of create'),
        ),
    ]
