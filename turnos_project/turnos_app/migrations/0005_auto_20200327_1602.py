# Generated by Django 2.2 on 2020-03-27 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turnos_app', '0004_auto_20200225_1545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dialaboral',
            name='medico',
        ),
        migrations.AddField(
            model_name='horariolaboral',
            name='medico',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='turnos_app.Medico'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dialaboral',
            name='dia',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Lunes'), (1, 'Martes'), (2, 'Miércoles'), (3, 'Jueves'), (4, 'Viernes'), (5, 'Sábado'), (6, 'Domingo')], unique=True),
        ),
        migrations.RemoveField(
            model_name='horariolaboral',
            name='dia_laboral',
        ),
        migrations.AddField(
            model_name='horariolaboral',
            name='dia_laboral',
            field=models.ManyToManyField(to='turnos_app.DiaLaboral'),
        ),
    ]
