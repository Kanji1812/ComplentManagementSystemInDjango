# Generated by Django 4.2.3 on 2023-08-29 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('s_id', models.AutoField(primary_key=True, serialize=False)),
                ('s_name', models.CharField(max_length=50)),
                ('enrollment_no', models.IntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('Div', models.CharField(max_length=3)),
                ('Roll_no', models.IntegerField(null=True)),
                ('password', models.CharField(max_length=100)),
                ('department', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.department')),
                ('type_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.type')),
            ],
        ),
    ]
