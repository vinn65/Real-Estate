# Generated by Django 3.2.3 on 2022-08-23 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20220823_0924'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='default.png', null=True, upload_to=''),
        ),
    ]
