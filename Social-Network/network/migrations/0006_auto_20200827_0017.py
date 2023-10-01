# Generated by Django 3.0.8 on 2020-08-26 18:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0005_auto_20200826_1413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes_count',
        ),
        migrations.AddField(
            model_name='post',
            name='likers',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
