# Generated by Django 4.2 on 2023-06-09 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0005_rename_m_link_moviecards_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moviecards',
            name='link',
        ),
    ]
