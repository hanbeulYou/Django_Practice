# Generated by Django 3.2.13 on 2022-10-05 01:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_comments'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
    ]