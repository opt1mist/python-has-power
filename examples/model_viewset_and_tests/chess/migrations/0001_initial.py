# Generated by Django 2.2 on 2019-04-12 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChessPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('birth_date', models.DateField()),
                ('pesel', models.TextField()),
                ('rodo_accepted', models.BooleanField()),
            ],
        ),
    ]
