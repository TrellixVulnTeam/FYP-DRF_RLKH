# Generated by Django 2.2.5 on 2019-10-30 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='username',
        ),
    ]
