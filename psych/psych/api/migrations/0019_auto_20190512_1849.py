# Generated by Django 2.2 on 2019-05-12 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20190512_1827'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ok_answer',
            old_name='question',
            new_name='quesId',
        ),
    ]
