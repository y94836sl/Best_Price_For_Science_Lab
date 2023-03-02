# Generated by Django 3.2.16 on 2023-02-26 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('category', models.CharField(choices=[('Stationary', 'Stationary'), ('Electronics', 'Electronics'), ('Chemical', 'Chemical'), ('Safety', 'Safety')], max_length=20, null=True)),
                ('quantity', models.PositiveIntegerField(null=True)),
            ],
        ),
    ]