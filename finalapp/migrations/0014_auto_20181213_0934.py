# Generated by Django 2.1.2 on 2018-12-13 04:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0013_document_countlikes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='countlikes',
            new_name='likes',
        ),
    ]
