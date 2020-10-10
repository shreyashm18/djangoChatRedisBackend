# Generated by Django 3.1.1 on 2020-10-10 13:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0010_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='related_group',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='related_group', to='chat.rooms'),
        ),
        migrations.AlterField(
            model_name='message',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='messages', to=settings.AUTH_USER_MODEL),
        ),
    ]
