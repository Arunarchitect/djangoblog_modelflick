# Generated by Django 4.2.1 on 2023-06-02 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0002_rename_tiltle_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Modelflick Blog', max_length=255),
        ),
    ]
