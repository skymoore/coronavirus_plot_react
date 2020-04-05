# Generated by Django 3.0.5 on 2020-04-05 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CaseType',
            fields=[
                ('case_type', models.CharField(choices=[('cnfd', 'confirmed'), ('rip', 'deaths'), ('rcvrd', 'recovered')], default='cnfd', max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='CountryRegion',
            fields=[
                ('region_country', models.CharField(default='', max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('county', models.CharField(default='', max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('latitude', models.CharField(max_length=50)),
                ('longitude', models.CharField(max_length=50)),
                ('friendly_name', models.CharField(max_length=100)),
                ('friendly_hash', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='corona_plots.County')),
            ],
        ),
        migrations.CreateModel(
            name='ProvinceState',
            fields=[
                ('province_state', models.CharField(default='', max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Plot',
            fields=[
                ('plot_name', models.CharField(default='', max_length=100, primary_key=True, serialize=False)),
                ('plot', models.CharField(default='', max_length=1000)),
                ('plot_case_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='corona_plots.CaseType')),
                ('plot_location', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='corona_plots.Location')),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='province_state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='corona_plots.ProvinceState'),
        ),
        migrations.AddField(
            model_name='location',
            name='region_country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='corona_plots.CountryRegion'),
        ),
        migrations.CreateModel(
            name='HistoricEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('count', models.IntegerField(default=0)),
                ('case_status_type_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='corona_plots.CaseType')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corona_plots.Location')),
            ],
        ),
    ]
