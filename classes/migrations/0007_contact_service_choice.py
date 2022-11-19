# Generated by Django 3.2 on 2022-03-31 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0006_auto_20220331_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='service_choice',
            field=models.CharField(blank=True, choices=[('HO', 'Hostel'), ('HA', 'Halfday'), ('FD', 'Fullday'), ('AS', 'After-school'), ('HD', 'Holiday'), ('NS', 'Night-stay')], max_length=2, null=True),
        ),
    ]
