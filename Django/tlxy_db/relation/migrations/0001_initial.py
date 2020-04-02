# Generated by Django 2.1.8 on 2020-04-01 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager_id', models.IntegerField()),
                ('manager_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_id', models.IntegerField()),
                ('school_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='manager',
            name='my_school',
            field=models.OneToOneField(on_delete=None, to='relation.School'),
        ),
    ]
