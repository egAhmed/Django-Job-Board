# Generated by Django 3.1.4 on 2020-12-22 10:36

from django.db import migrations, models
import job.models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='image',
            field=models.ImageField(default='', upload_to=job.models.image_upload),
            preserve_default=False,
        ),
    ]
