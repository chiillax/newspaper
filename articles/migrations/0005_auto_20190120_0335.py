# Generated by Django 2.1 on 2019-01-19 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_comment_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='text',
        ),
    ]
