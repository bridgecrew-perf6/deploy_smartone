# Generated by Django 4.0 on 2022-01-13 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_remove_feedback_user_surname_feedback_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='title',
            new_name='city',
        ),
        migrations.AddField(
            model_name='feedback',
            name='email',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
