# Generated by Django 3.0.2 on 2020-05-17 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='body',
            new_name='Memo',
        ),
    ]
