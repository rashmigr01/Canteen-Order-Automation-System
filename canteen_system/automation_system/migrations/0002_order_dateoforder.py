# Generated by Django 4.0.3 on 2022-03-21 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automation_system', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='DateOfOrder',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
