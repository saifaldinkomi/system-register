# Generated by Django 5.0.4 on 2024-05-22 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_students_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('description', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
