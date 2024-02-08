# Generated by Django 5.0.2 on 2024-02-07 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rollNo', models.IntegerField()),
                ('section', models.FloatField(blank=True, null=True)),
                ('phoneNo', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
            ],
        ),
    ]