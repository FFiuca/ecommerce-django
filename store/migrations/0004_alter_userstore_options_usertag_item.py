# Generated by Django 4.1.7 on 2023-09-28 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_usertag_usertag_store_usert_tag_nam_1ec3bb_idx'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userstore',
            options={'ordering': ['store_name']},
        ),
        migrations.AddField(
            model_name='usertag',
            name='item',
            field=models.ManyToManyField(related_name='user_tag_item', to='store.useritem'),
        ),
    ]
