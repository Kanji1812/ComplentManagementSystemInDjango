# Generated by Django 4.2.3 on 2023-08-29 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_complaint_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='user_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.type'),
        ),
    ]
