# Generated by Django 4.2.2 on 2023-07-23 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0031_personaldata_address_personaldata_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldata',
            name='summary',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
