# Generated by Django 4.2.2 on 2023-07-18 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0021_remove_personaldata_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldata',
            name='logo',
            field=models.TextField(blank=True, max_length=15, null=True),
        ),
    ]
