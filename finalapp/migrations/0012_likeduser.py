# Generated by Django 2.1.2 on 2018-12-13 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0011_auto_20181118_1615'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikedUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('image', models.URLField(max_length=100)),
            ],
        ),
    ]
