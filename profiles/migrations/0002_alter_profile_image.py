# Generated by Django 3.2.20 on 2023-08-13 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../https://res.cloudinary.com/dehoeoirf/image/upload/v1691421814/default_profile_dggwuo.jpg', upload_to='images/'),
        ),
    ]
