# Generated by Django 4.2.6 on 2023-10-23 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crmModule', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sponsor',
            name='agreement',
        ),
    ]