# Generated by Django 2.2.1 on 2020-02-13 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_auto_20200213_1333'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='出版社名字')),
                ('address', models.CharField(max_length=32, verbose_name='出版社地址')),
            ],
            options={
                'db_table': 'publish',
            },
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name_plural': 'user'},
        ),
    ]
