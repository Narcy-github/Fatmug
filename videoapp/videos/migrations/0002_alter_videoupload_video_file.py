# Generated by Django 5.1.1 on 2024-09-16 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoupload',
            name='video_file',
            field=models.FileField(upload_to='media/videos'),
        ),
    ]
