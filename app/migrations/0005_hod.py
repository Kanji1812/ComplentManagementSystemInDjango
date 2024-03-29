# Generated by Django 4.2.3 on 2023-08-29 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_faculty_password_alter_faculty_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='HOD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hod_Name', models.CharField(max_length=55)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.department')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.type')),
            ],
            options={
                'db_table': 'HOD',
            },
        ),
    ]
