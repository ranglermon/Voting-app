# Generated by Django 2.0.7 on 2018-07-22 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0006_auto_20180720_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='election',
            name='Number_Of_Alternatives',
            field=models.IntegerField(default=1),
        ),
    ]
