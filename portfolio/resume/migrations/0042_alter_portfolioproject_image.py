# Generated by Django 4.2.2 on 2023-07-25 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0041_portfolioproject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolioproject',
            name='image',
            field=models.ImageField(upload_to='resume/static/img/portfolio'),
        ),
    ]