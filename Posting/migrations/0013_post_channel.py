# Generated by Django 4.0.4 on 2022-04-19 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Channels', '0003_alter_channel_username'),
        ('Posting', '0012_rename_body_post_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='channel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='user_posts', to='Channels.channel'),
            preserve_default=False,
        ),
    ]
