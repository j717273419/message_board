# Generated by Django 2.0.2 on 2018-03-05 15:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=20, verbose_name='姓名')),
                ('email', models.EmailField(blank=True, default='', max_length=254, verbose_name='邮箱')),
                ('text', models.TextField(blank=True, default='', verbose_name='留言内容')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '留言板内容',
                'verbose_name_plural': '留言板列表',
                'db_table': 'meassage',
                'ordering': ['create_time'],
            },
        ),
    ]
