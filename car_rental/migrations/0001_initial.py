# Generated by Django 5.0.3 on 2024-03-26 05:33

import datetime
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('PATH', '0007_customuser_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_type', models.CharField(choices=[('sedan', 'Sedan'), ('suv', 'SUV'), ('truck', 'Truck'), ('van', 'Van'), ('sports', 'Sports')], default='sedan', max_length=20)),
                ('make', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('year', models.PositiveIntegerField()),
                ('daily_rate', models.DecimalField(decimal_places=2, max_digits=8)),
                ('available', models.BooleanField(default=True)),
                ('color', models.CharField(default='unknown', max_length=50)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='car_photos/')),
                ('seats', models.PositiveIntegerField(default='5')),
                ('fuel_type', models.CharField(choices=[('petrol', 'petrol'), ('diesel', 'diesel')], default='petrol', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('email', models.EmailField(default='', max_length=80, unique=True)),
                ('password', models.CharField(default='', max_length=128)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(default='', max_length=100)),
                ('country', models.CharField(blank=True, default='', max_length=100)),
                ('address', models.CharField(blank=True, default='', max_length=100)),
                ('city', models.CharField(blank=True, default='', max_length=100)),
                ('state', models.CharField(blank=True, default='', max_length=100)),
                ('postal_code', models.CharField(blank=True, default='', max_length=100)),
                ('mobile', models.CharField(blank=True, default='', max_length=11)),
                ('issueing_country', models.CharField(blank=True, choices=[('Canada', 'Canada'), ('USA', 'USA')], default='Windsor', max_length=100)),
                ('dl_number', models.CharField(blank=True, default='', max_length=100)),
                ('expiry_date', models.DateTimeField(blank=True, null=True)),
                ('birth_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InsurancePolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_number', models.CharField(max_length=100)),
                ('provider_name', models.CharField(max_length=100)),
                ('coverage_start_date', models.DateField()),
                ('coverage_end_date', models.DateField()),
                ('premium_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('deductible_amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('review_text', models.TextField()),
                ('date_posted', models.DateField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_rental.car')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_rental.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='LicenseDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issuing_country', models.CharField(max_length=100)),
                ('issuing_authority', models.CharField(max_length=100)),
                ('birth_date', models.DateField(default=datetime.date(2024, 3, 26))),
                ('driving_license_number', models.CharField(max_length=100)),
                ('issue_date', models.DateField(default=datetime.date(2024, 3, 26))),
                ('expiry_date', models.DateField(default=datetime.date(2024, 3, 26))),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PATH.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='RentalReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rental_start_date', models.DateField(default=django.utils.timezone.now)),
                ('rental_end_date', models.DateField(default=django.utils.timezone.now)),
                ('pickup_time', models.TimeField(default='00:00')),
                ('return_time', models.TimeField(default='00:00')),
                ('pickup_location', models.CharField(choices=[('London', 'London'), ('Windsor', 'Windsor'), ('Toronto', 'Toronto'), ('Hamilton', 'Hamilton')], default='Windsor', max_length=100)),
                ('car_type', models.CharField(choices=[('sedan', 'Sedan'), ('suv', 'SUV'), ('truck', 'Truck'), ('van', 'Van'), ('sports', 'Sports')], default='', max_length=20)),
                ('car_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='car_rental.car')),
                ('customer', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='PATH.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='RentalInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.CharField(max_length=100, unique=True)),
                ('issue_date', models.DateField()),
                ('due_date', models.DateField()),
                ('amount_due', models.DecimalField(decimal_places=2, max_digits=10)),
                ('paid', models.BooleanField(default=False)),
                ('rental_reservation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='car_rental.rentalreservation')),
            ],
        ),
        migrations.CreateModel(
            name='RentalTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateField()),
                ('transaction_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method', models.CharField(max_length=100)),
                ('transaction_status', models.CharField(max_length=100)),
                ('rental_reservation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='car_rental.rentalreservation')),
            ],
        ),
    ]
