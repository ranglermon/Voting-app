# Generated by Django 2.0.7 on 2018-07-20 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0004_auto_20180720_1030'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alternative',
            old_name='Election_Number',
            new_name='Election_ID',
        ),
        migrations.RenameField(
            model_name='election',
            old_name='Election_Number',
            new_name='Election_ÌD',
        ),
        migrations.RenameField(
            model_name='vote',
            old_name='Election_Number',
            new_name='Election_ID',
        ),
        migrations.AddField(
            model_name='election',
            name='Name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
