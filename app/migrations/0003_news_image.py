# Generated by Django 4.0 on 2021-12-29 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_news_news_subtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='uploads/'),
        ),
    ]
