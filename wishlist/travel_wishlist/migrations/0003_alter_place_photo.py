# Generated by Django 5.0.3 on 2024-05-06 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_wishlist', '0002_place_date_visited_place_notes_place_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='user_images/'),
        ),
    ]
