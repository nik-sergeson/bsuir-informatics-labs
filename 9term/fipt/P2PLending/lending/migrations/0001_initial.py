from __future__ import unicode_literals

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djmoney.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MoneyProposalAd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('rate', models.FloatField()),
                ('min_amount_currency', djmoney.models.fields.CurrencyField(choices=[('BYR', 'Belarussian Ruble')], default='BYR', editable=False, max_length=3)),
                ('min_amount', djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0.0'), max_digits=10)),
                ('max_amount_currency', djmoney.models.fields.CurrencyField(choices=[('BYR', 'Belarussian Ruble')], default='BYR', editable=False, max_length=3)),
                ('max_amount', djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0.0'), max_digits=10)),
                ('min_term', models.DurationField()),
                ('max_term', models.DurationField()),
                ('end', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MoneyRequestAd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('amount_currency', djmoney.models.fields.CurrencyField(choices=[('BYR', 'Belarussian Ruble')], default='BYR', editable=False, max_length=3)),
                ('term', models.DurationField()),
                ('amount', djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0.0'), max_digits=10)),
                ('return_probability', models.FloatField(null=True)),
                ('end', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
