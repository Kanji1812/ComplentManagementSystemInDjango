# Generated by Django 4.2.3 on 2023-08-29 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_complaint_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='user_type',
            field=models.ForeignKey(default=4, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.type'),
        ),
    ]
