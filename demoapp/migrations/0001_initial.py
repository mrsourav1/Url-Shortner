# Generated by Django 4.0.4 on 2022-05-13 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DemoUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_url', models.CharField(max_length=100)),
                ('long_url', models.URLField(verbose_name='URL')),
            ],
        ),
    ]
