# Generated by Django 5.1.2 on 2024-11-30 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmwebsite', '0002_instructor_profile_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
