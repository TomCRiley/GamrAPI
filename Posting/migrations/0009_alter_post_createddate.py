# Generated by Django 4.0.4 on 2022-04-19 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posting', '0008_alter_post_createddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='createdDate',
            field=models.DateField(null=True),
        ),
    ]
