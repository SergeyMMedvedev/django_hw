# Generated by Django 4.1.4 on 2022-12-27 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0004_alter_phone_image_alter_phone_lte_exists_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='phone',
            name='lte_exists',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='phone',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='release_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
