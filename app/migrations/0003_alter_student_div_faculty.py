# Generated by Django 4.2.3 on 2023-08-29 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Div',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F')], default='A', max_length=1),
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=254)),
                ('department_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.department')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.subject')),
                ('type', models.ForeignKey(default='faculty', on_delete=django.db.models.deletion.CASCADE, to='app.type')),
            ],
        ),
    ]
