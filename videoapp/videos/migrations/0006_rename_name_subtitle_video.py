# Generated by Django 5.1.1 on 2024-09-17 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_alter_subtitle_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subtitle',
            old_name='name',
            new_name='video',
        ),
    ]
