# Generated by Django 3.0.5 on 2020-04-30 20:11

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nip', models.BigIntegerField(blank=True, null=True)),
                ('regon', models.BigIntegerField(blank=True, null=True)),
                ('company_start_date', models.DateTimeField(default=datetime.datetime(2020, 4, 30, 20, 11, 32, 928996, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(default='00000000000000000000000000', max_length=28)),
                ('country', models.CharField(default='Poland', max_length=28)),
                ('ballance', models.DecimalField(decimal_places=2, max_digits=19)),
                ('creation_date', models.DateTimeField(blank=True, null=True)),
                ('active', models.BooleanField(blank=True, null=True)),
                ('is_company', models.BooleanField(default=False)),
                ('company_data', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wallets.CompanyData')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
