# Generated by Django 3.2.5 on 2022-01-18 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baby', '0006_auto_20220118_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/photos/'),
        ),
    ]
