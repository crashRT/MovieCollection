# Generated by Django 4.1 on 2023-03-12 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='creators',
            new_name='creator',
        ),
    ]
