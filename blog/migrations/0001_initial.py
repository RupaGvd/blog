# Generated by Django 4.0 on 2024-08-05 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, upload_to='photos')),
                ('desc', models.TextField(max_length=350)),
            ],
        ),
    ]
