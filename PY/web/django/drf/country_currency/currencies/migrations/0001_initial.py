# Generated by Django 3.1.7 on 2021-08-09 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('currency', models.CharField(max_length=20)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]