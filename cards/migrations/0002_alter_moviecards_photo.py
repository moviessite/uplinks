# Generated by Django 4.2 on 2023-06-08 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviecards',
            name='photo',
            field=models.FileField(default=None, max_length=400, null=True, upload_to='cardmedia/'),
        ),
    ]
