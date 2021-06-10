# Generated by Django 3.2.4 on 2021-06-10 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210610_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinghistory',
            name='booked_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='History', to='home.user'),
        ),
        migrations.AlterField(
            model_name='bookinghistory',
            name='house_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='History', to='home.home'),
        ),
    ]