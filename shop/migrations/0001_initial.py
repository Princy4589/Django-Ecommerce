# Generated by Django 3.2.4 on 2021-10-04 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_ctg', models.CharField(max_length=200)),
                ('date_ajout_ctg', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-date_ajout_ctg'],
            },
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_produit', models.CharField(max_length=200)),
                ('prix_produit', models.FloatField()),
                ('description_produit', models.TextField()),
                ('image_produit', models.CharField(max_length=5000)),
                ('date_ajout_prod', models.DateTimeField(auto_now=True)),
                ('categorie_produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categorie', to='shop.categorie')),
            ],
            options={
                'ordering': ['-date_ajout_prod'],
            },
        ),
    ]