# Generated by Django 2.0 on 2020-01-07 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0012_auto_20191204_0944'),
    ]

    operations = [
        migrations.AddField(
            model_name='voting',
            name='blank_vote',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
