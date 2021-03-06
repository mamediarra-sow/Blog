# Generated by Django 2.2.11 on 2020-03-12 23:26

import MonBlog.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auteur', models.CharField(max_length=255)),
                ('publication', djongo.models.fields.EmbeddedField(model_container=MonBlog.models.Publication, null=True)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auteur', models.CharField(max_length=255)),
                ('publication', djongo.models.fields.EmbeddedField(model_container=MonBlog.models.Publication, null=True)),
                ('on_click', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('categorie', models.CharField(choices=[('Makeup steps', 'Makeup steps'), ('Makeup peau noire', 'Makeup peau noire'), ('Makeup peau claire', 'Makeup peau claire'), ('Makeup soft', 'Makeup soft'), ('Makeup fantaisie', 'Makeup fantaisie'), ('Conseils beauté', 'Conseils beauté')], max_length=255)),
                ('description', models.TextField()),
                ('date', models.DateTimeField()),
                ('media', models.FileField(upload_to='')),
                ('like', models.IntegerField(default='null')),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
