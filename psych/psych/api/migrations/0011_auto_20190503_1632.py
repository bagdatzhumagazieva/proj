# Generated by Django 2.2 on 2019-05-03 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20190503_1626'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='name',
            new_name='question',
        ),
    ]