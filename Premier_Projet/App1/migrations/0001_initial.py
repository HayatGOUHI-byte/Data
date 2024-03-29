# Generated by Django 4.2.6 on 2024-02-17 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('adresse', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('code_produit', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_commande', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App1.client')),
                ('produits', models.ManyToManyField(to='App1.produit')),
            ],
        ),
    ]
