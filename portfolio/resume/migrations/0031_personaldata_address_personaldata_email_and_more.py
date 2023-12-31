# Generated by Django 4.2.2 on 2023-07-23 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0030_education_specialization'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldata',
            name='address',
            field=models.TextField(blank=True, max_length=35, null=True),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='summary',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='tel',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
