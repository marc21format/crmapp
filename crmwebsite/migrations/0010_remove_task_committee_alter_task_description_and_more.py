# Generated by Django 5.1.2 on 2024-12-02 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmwebsite', '0009_task_status_alter_task_committee_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='committee',
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(max_length=500),
        ),
        migrations.DeleteModel(
            name='CommitteeMember',
        ),
    ]
