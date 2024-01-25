# Generated by Django 5.0.1 on 2024-01-25 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leaveRequestId', models.CharField(default=None, max_length=255)),
                ('userId', models.CharField(default=None, max_length=255)),
                ('startDate', models.DateTimeField(default=None)),
                ('endDate', models.DateTimeField(default=None)),
                ('reason', models.CharField(default=None, max_length=255)),
                ('status', models.CharField(default=None, max_length=255)),
                ('rejectedReason', models.CharField(default=None, max_length=255)),
                ('remainingDay', models.CharField(default=None, max_length=255)),
            ],
        ),
    ]