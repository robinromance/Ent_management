# Generated by Django 5.0.6 on 2024-06-11 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_rno', models.IntegerField()),
                ('s_name', models.CharField(max_length=50)),
                ('s_class', models.IntegerField()),
                ('s_address', models.CharField(max_length=50)),
            ],
        ),
    ]
