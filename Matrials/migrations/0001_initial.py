# Generated by Django 4.1.2 on 2022-10-16 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatrialInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoiceNumber', models.CharField(max_length=200)),
                ('dateRecieved', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=50)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matrial', to='Projects.project')),
            ],
        ),
    ]
