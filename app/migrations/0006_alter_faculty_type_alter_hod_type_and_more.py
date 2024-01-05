# Generated by Django 4.2.3 on 2023-08-29 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_hod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='type',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='app.type'),
        ),
        migrations.AlterField(
            model_name='hod',
            name='type',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='app.type'),
        ),
        migrations.AlterField(
            model_name='student',
            name='type_data',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.type'),
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('director_name', models.CharField(max_length=55)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=55)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.type')),
            ],
            options={
                'db_table': 'director',
            },
        ),
    ]
