# Generated by Django 4.1.7 on 2023-09-03 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0002_alter_usertype_created_alter_usertype_user_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usertype',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='usertype',
            old_name='updated',
            new_name='updated_at',
        ),
    ]
