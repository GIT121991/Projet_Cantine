# Generated by Django 4.2.4 on 2023-10-25 14:38

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
                ('classe_name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Niveau',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(choices=[('P', 'Primaire'), ('C', 'Collège'), ('L', 'Lycée')], default='C', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastname', models.CharField(max_length=50)),
                ('firstname', models.CharField(max_length=50)),
                ('genre', models.CharField(choices=[('F', 'Féminin'), ('M', 'Masculin')], default='M', max_length=1)),
                ('user_type', models.CharField(choices=[(1, 'Admin'), (2, 'Gérand'), (3, 'Agent'), (4, 'Eleve'), (5, 'Enseignant')], default=1, max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('classe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App_Cantine.classes')),
            ],
        ),
        migrations.AddField(
            model_name='classes',
            name='niveau',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Cantine.niveau'),
        ),
    ]
