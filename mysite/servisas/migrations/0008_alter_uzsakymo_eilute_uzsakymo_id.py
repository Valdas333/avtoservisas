# Generated by Django 4.0.5 on 2022-06-23 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servisas', '0007_alter_automobilio_modelis_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uzsakymo_eilute',
            name='uzsakymo_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='uzsakymas', to='servisas.uzsakymas'),
        ),
    ]
