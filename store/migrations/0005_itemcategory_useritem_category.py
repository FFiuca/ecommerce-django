# Generated by Django 4.1.7 on 2023-09-28 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0018_alter_status_created_at_alter_usertype_created_at'),
        ('store', '0004_alter_userstore_options_usertag_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pivot_item_category', to='master.category')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pivot_category_item', to='store.useritem')),
            ],
        ),
        migrations.AddField(
            model_name='useritem',
            name='category',
            field=models.ManyToManyField(related_name='rel_item_category', through='store.ItemCategory', to='master.category'),
        ),
    ]
