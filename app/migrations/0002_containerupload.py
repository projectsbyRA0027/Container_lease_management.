# Generated by Django 4.0.7 on 2023-01-13 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='containerupload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Containertype', models.CharField(max_length=30)),
                ('Containerprice', models.CharField(max_length=30)),
                ('Containercount', models.CharField(max_length=30)),
                ('Lessorname', models.CharField(max_length=30)),
                ('picture', models.FileField(default=0, upload_to='')),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
