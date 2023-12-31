# Generated by Django 4.2.4 on 2023-11-20 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('classe_name', models.CharField(max_length=50, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Niveau',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(choices=[('P', 'Primaire'), ('C', 'Collège'), ('L', 'Lycée')], default='C', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='TypeAbonnements',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('Aucun', 'Aucun'), ('3 jours', '3 jours'), ('Hebdomadaire', 'Hebdomadaire'), ('Mensuel', 'Mensuel'), ('Trimestriel', 'Trimestriel')], default='3 jours', max_length=20, unique=True)),
                ('priceTeacher', models.IntegerField(default=1000)),
                ('priceStudent', models.IntegerField(default=1000)),
                ('duree_jours', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastname', models.CharField(max_length=50)),
                ('firstname', models.CharField(max_length=50)),
                ('genre', models.CharField(choices=[('F', 'Féminin'), ('M', 'Masculin')], default='M', max_length=1)),
                ('user_type', models.CharField(choices=[('Admin', 'Admin'), ('Gérand', 'Gérand'), ('Agent', 'Agent'), ('Eleve', 'Eleve'), ('Enseignant', 'Enseignant')], default='Eleve', max_length=50)),
                ('is_abonne', models.BooleanField(default=False)),
                ('date_abonnement', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('classe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App_Cantine.classes')),
                ('type_abonnement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App_Cantine.typeabonnements')),
            ],
        ),
        migrations.AddField(
            model_name='classes',
            name='niveau',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Cantine.niveau'),
        ),
    ]
