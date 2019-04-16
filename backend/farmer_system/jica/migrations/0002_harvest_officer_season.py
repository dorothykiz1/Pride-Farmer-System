# Generated by Django 2.2 on 2019-04-16 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jica', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Harvest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('season', models.CharField(max_length=50)),
                ('Area', models.CharField(max_length=50)),
                ('harvest', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Officer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('loginID', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=50)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jica.District', verbose_name='')),
                ('subcountry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jica.Subcounty', verbose_name='')),
            ],
        ),
    ]