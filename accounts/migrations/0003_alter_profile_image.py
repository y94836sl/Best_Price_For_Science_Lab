# Generated by Django 3.2.16 on 2023-03-05 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='defaultProfileImage.jpeg', null=True, upload_to='Profile_Images'),
        ),
    ]