# Generated by Django 5.2.1 on 2025-05-25 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0002_message_avatar_alter_message_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='admin_reply',
            field=models.TextField(blank=True, null=True),
        ),
    ]
