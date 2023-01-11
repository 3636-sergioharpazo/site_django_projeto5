# Generated by Django 4.0.8 on 2023-01-10 23:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('is_published', models.BooleanField(default=True)),
                ('date_created', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
