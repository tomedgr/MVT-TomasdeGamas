# Generated by Django 4.0.5 on 2022-06-25 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primerasvistas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Madre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
                ('fecha_nacimiento', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Padre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
                ('fecha_nacimiento', models.DateField(null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Perro',
            new_name='Hermana',
        ),
        migrations.RenameField(
            model_name='hermana',
            old_name='fecha_creacion',
            new_name='fecha_nacimiento',
        ),
    ]
