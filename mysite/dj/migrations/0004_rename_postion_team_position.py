# Generated by Django 5.1 on 2024-08-28 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dj', '0003_rename_disc_team_discription_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='postion',
            new_name='position',
        ),
    ]
