# Generated by Django 3.2.5 on 2021-07-27 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookinstance',
            old_name='staus',
            new_name='status',
        ),
    ]
