# Generated by Django 4.1.2 on 2022-11-28 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_rename_name_category_category_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postcategory',
            old_name='commentPost',
            new_name='post',
        ),
    ]
