# Generated by Django 3.0.3 on 2020-02-12 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteConfiguration',
            fields=[
                ('name', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('style', models.CharField(choices=[('padrao', 'Padrão'), ('cosmo', 'Cosmo'), ('flatly', 'Flatly'), ('litera', 'Litera'), ('lumen', 'Lumen'), ('materia', 'Materia'), ('sketchy', 'Sketchy')], default='padrao', max_length=15)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_query_name='site_configurations', to='auth.Group', unique=True)),
            ],
        ),
    ]