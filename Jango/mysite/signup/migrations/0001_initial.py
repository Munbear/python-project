# Generated by Django 3.1.5 on 2021-01-25 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, verbose_name='Username')),
                ('password', models.CharField(max_length=64, verbose_name='Password')),
                ('register_dttm', models.DateTimeField(auto_now_add=True, verbose_name='RegisterTime')),
            ],
            options={
                'db_table': 'TestUser',
            },
        ),
    ]
