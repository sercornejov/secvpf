# Generated by Django 4.2.7 on 2023-11-13 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfapp', '0003_alter_geninfo_userid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='geninfo',
            old_name='userid',
            new_name='user',
        ),
    ]