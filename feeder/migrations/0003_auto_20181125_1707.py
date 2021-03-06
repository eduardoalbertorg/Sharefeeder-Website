# Generated by Django 2.0.2 on 2018-11-25 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('feeder', '0002_auto_20181125_1702'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credential',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=85)),
                ('password', models.CharField(max_length=85)),
            ],
        ),
        migrations.CreateModel(
            name='Feeder',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=85)),
            ],
        ),
        migrations.CreateModel(
            name='Galileo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=85)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=85)),
                ('credential', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feeder.Credential')),
            ],
        ),
        migrations.AddField(
            model_name='feeder',
            name='galileo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feeder.Galileo'),
        ),
    ]
