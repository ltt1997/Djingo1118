# Generated by Django 2.2.1 on 2020-03-06 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Sheller', '0009_codeinfo'),
        ('Buyer', '0002_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAdress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=16, verbose_name='收件人')),
                ('adress', models.TextField(verbose_name='详细地址')),
                ('zip_code', models.CharField(max_length=8, verbose_name='邮编')),
                ('phone', models.CharField(max_length=11, verbose_name='手机号')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sheller.regUser')),
            ],
        ),
    ]
