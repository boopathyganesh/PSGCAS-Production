# Generated by Django 4.1.7 on 2023-04-26 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('superlee', '0007_alter_intern_atn_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='intern_atn',
            unique_together={('reg_no', 'Date')},
        ),
    ]
