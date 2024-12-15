# Generated by Django 4.1.3 on 2023-09-02 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateurs', '0001_initial'),
        ('departement', '0001_initial'),
        ('emplois_temps', '0004_alter_seance_cour_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seance_td',
            name='cour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emplois_temps.cour'),
        ),
        migrations.AlterField(
            model_name='seance_td',
            name='enseignant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utilisateurs.enseignant'),
        ),
        migrations.AlterField(
            model_name='seance_td',
            name='filiere',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departement.filiere'),
        ),
        migrations.AlterField(
            model_name='seance_td',
            name='group_td',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emplois_temps.group_td'),
        ),
    ]