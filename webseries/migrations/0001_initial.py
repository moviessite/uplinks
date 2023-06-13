# Generated by Django 4.2 on 2023-06-08 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='webcards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('w_photo', models.FileField(default=None, max_length=700, null=True, upload_to='webmedia/')),
                ('w_title', models.CharField(max_length=100)),
                ('w_descript', models.CharField(max_length=1000)),
                ('w_update', models.CharField(max_length=50)),
            ],
        ),
    ]
