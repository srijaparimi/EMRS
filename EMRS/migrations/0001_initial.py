# Generated by Django 3.0.4 on 2020-03-07 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('url', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'seen_movies',
            },
        ),
    ]
