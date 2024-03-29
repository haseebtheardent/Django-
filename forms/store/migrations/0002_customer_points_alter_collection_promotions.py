# Generated by Django 4.0 on 2024-03-20 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='points',
            field=models.IntegerField(default=50),
        ),
        migrations.AlterField(
            model_name='collection',
            name='promotions',
            field=models.ManyToManyField(to='store.Promotion'),
        ),
    ]
