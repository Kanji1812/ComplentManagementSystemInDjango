# Generated by Django 4.2.4 on 2023-09-11 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_complaint_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.OneToOneField(db_column='department', on_delete=django.db.models.deletion.CASCADE, to='app.department'),
        ),
        migrations.AlterField(
            model_name='student',
            name='type_data',
            field=models.ForeignKey(db_column='type_data', default=1, on_delete=django.db.models.deletion.CASCADE, to='app.type'),
        ),
    ]
