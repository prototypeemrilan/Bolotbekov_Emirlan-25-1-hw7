# Generated by Django 4.1.7 on 2023-02-23 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='product',
        ),
    ]
