# Generated by Django 5.0.1 on 2024-03-06 08:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='song',
            fields=[
                ('song_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('singer', models.CharField(max_length=500)),
                ('tags', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='media/images')),
                ('Song', models.FileField(upload_to='media/songs')),
                ('movie', models.CharField(default='', max_length=1000)),
                ('categories', models.CharField(choices=[('TREANDING', 'treanding'), ('HINDI', 'Hindi'), ('ENGLISH', 'English'), ('MARATHI', 'Marathi'), ('DEVOTIONAL', 'devotional')], default='NA', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music_id', models.CharField(default='', max_length=20000000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]