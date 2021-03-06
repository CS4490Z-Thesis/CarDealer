# Generated by Django 3.0.6 on 2020-09-11 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_auto_20200910_2055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='miles',
            new_name='kilometers',
        ),
        migrations.AddField(
            model_name='car',
            name='bodytype',
            field=models.CharField(default='none', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='colour',
            field=models.CharField(default='none', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='drivetrain',
            field=models.CharField(default='none', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.CharField(default='none', max_length=50),
            preserve_default=False,
        ),
    ]
