# Generated by Django 5.1 on 2024-08-22 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_employee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='resignetion',
            new_name='designetion',
        ),
    ]
