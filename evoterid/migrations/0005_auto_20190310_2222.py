# Generated by Django 2.1.5 on 2019-03-10 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evoterid', '0004_auto_20190310_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.FileField(upload_to=''),
        ),
    ]
