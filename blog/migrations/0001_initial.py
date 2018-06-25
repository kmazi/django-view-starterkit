# Generated by Django 2.0.6 on 2018-06-21 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('article_id', models.AutoField(primary_key=True, serialize=False)),
                ('article_heading', models.CharField(max_length=250)),
                ('article_body', models.TextField()),
                ('article_conclusion', models.CharField(max_length=250)),
            ],
        ),
    ]
