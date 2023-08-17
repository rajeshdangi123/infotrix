# Generated by Django 4.2.3 on 2023-07-08 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email_field', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
