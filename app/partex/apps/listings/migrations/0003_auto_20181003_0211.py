# Generated by Django 2.1 on 2018-10-03 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_listing_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='base_item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listings', to='listings.AbstractItem'),
        ),
    ]
