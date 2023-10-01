# Generated by Django 3.0.8 on 2020-08-26 19:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0006_auto_20200827_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='savers',
            field=models.ManyToManyField(related_name='saved', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Saved',
        ),
    ]
