# Generated by Django 3.1.6 on 2021-02-14 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warsztat', '0002_reservation'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='comment',
            field=models.TextField(default=True),
            preserve_default=False,
        ),
    ]
