# Generated by Django 2.2.1 on 2020-02-26 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Sheller', '0006_reguser_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_label', models.CharField(max_length=32, verbose_name='类型标签')),
                ('type_decsription', models.TextField(verbose_name='类型描述')),
                ('type_picture', models.ImageField(default='img/01.jpg', upload_to='img', verbose_name='类型图片')),
            ],
            options={
                'db_table': 'goods_type',
            },
        ),
        migrations.AddField(
            model_name='goods',
            name='goods_picture',
            field=models.ImageField(default='img/gtl.jpg', upload_to='img', verbose_name='商品图片'),
        ),
        migrations.AddField(
            model_name='goods',
            name='goods_store',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Sheller.regUser'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='goods',
            name='goods_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Sheller.GoodsType'),
            preserve_default=False,
        ),
    ]
