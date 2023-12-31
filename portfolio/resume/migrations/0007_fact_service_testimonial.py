# Generated by Django 4.2.2 on 2023-07-06 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0006_rename_github_socialmedia_platform_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.TextField()),
                ('service_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('proffesion', models.TextField()),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
