# Generated by Django 2.2.1 on 2020-02-25 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sheller', '0005_auto_20200225_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='reguser',
            name='user_type',
            field=models.IntegerField(default=1, verbose_name='用户身份'),
        ),
    ]