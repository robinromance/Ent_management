# Generated by Django 5.0.6 on 2024-06-11 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ent_item', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='s_rno',
        ),
    ]
