# Generated by Django 2.2.4 on 2019-08-26 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapi', '0002_auto_20190826_0635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='image',
            field=models.ImageField(default='images/no-img.jpg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='music',
            name='musicFile',
            field=models.FileField(default='audio/def.mp3', upload_to='audio/'),
        ),
    ]
