# Generated by Django 4.1.5 on 2023-01-31 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='emailid',
            new_name='email_id',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='fistname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='lastname',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='phonenumber',
            new_name='phone_number',
        ),
    ]
