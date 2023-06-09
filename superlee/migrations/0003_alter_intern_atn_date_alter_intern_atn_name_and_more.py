# Generated by Django 4.1.7 on 2023-04-24 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('superlee', '0002_alter_intern_atn_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intern_atn',
            name='Date',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='intern_atn',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superlee.intern_db'),
        ),
        migrations.AlterField(
            model_name='intern_atn',
            name='reg_no',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='intern_db',
            name='name',
            field=models.CharField(blank=True, max_length=150, unique=True),
        ),
    ]
