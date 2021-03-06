# Generated by Django 3.0.6 on 2020-05-17 09:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('timeStamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
