# Generated by Django 5.0 on 2024-03-16 17:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Resturant', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='resturantcomments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='resturantimages',
            name='resturant_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Resturant.resturant'),
        ),
        migrations.AddField(
            model_name='resturantreservation',
            name='resturant_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Resturant.resturant'),
        ),
        migrations.AddField(
            model_name='resturantreservation',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='resturantreservationidimage',
            name='reservation_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Resturant.resturantreservation'),
        ),
    ]