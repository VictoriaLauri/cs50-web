# Generated by Django 5.0.4 on 2024-05-02 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights_schedule', '0002_airport_remove_flight_arrival_city_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=50)),
                ('last', models.CharField(max_length=50)),
                ('flights', models.ManyToManyField(blank=True, related_name='passengers', to='flights_schedule.flight')),
            ],
        ),
    ]
