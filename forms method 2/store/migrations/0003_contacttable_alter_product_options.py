# Generated by Django 4.0 on 2024-03-25 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_customer_points_alter_collection_promotions'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['id']},
        ),
    ]