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
        ('lending', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoneyPartnership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('STR', 'Started'), ('FIN', 'Finished'), ('CAN', 'Cancelled')], default='STR', max_length=3)),
                ('amount_currency', djmoney.models.fields.CurrencyField(choices=[('BYR', 'Belarussian Ruble')], default='BYR', editable=False, max_length=3)),
                ('amount', djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0.0'), max_digits=10)),
                ('dept_currency', djmoney.models.fields.CurrencyField(choices=[('BYR', 'Belarussian Ruble')], default='BYR', editable=False, max_length=3)),
                ('annuity_payment_currency', djmoney.models.fields.CurrencyField(choices=[('BYR', 'Belarussian Ruble')], default='BYR', editable=False, max_length=3)),
                ('dept', djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0'), max_digits=10)),
                ('annuity_payment', djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0.0'), max_digits=10)),
                ('rate', models.FloatField()),
                ('term', models.DurationField()),
                ('last_annuity_payment', models.DateField(null=True)),
                ('last_dept_day_included', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MoneyProposalPartnershipSuggestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('amount_currency', djmoney.models.fields.CurrencyField(choices=[('BYR', 'Belarussian Ruble')], default='BYR', editable=False, max_length=3)),
                ('term', models.DurationField()),
                ('amount', djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0.0'), max_digits=10)),
                ('return_probability', models.FloatField(null=True)),
                ('status', models.CharField(choices=[('SUG', 'Suggested'), ('ACC', 'Accepted'), ('REJ', 'Rejected')], default='SUG', max_length=3)),
                ('proposal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lending.MoneyProposalAd')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MoneyRequestPartnershipSuggestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('rate', models.FloatField()),
                ('status', models.CharField(choices=[('SUG', 'Suggested'), ('ACC', 'Accepted'), ('REJ', 'Rejected')], default='SUG', max_length=3)),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lending.MoneyRequestAd')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MoneyTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_currency', djmoney.models.fields.CurrencyField(choices=[('BYR', 'Belarussian Ruble')], default='BYR', editable=False, max_length=3)),
                ('amount', djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0'), max_digits=10)),
                ('transaction_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('CRE', 'Created'), ('EXC', 'Executed')], default='CRE', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='MoneyProposalPartnership',
            fields=[
                ('moneypartnership_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='partnership.MoneyPartnership')),
                ('proposal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='lending.MoneyProposalAd')),
                ('suggestion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='partnership.MoneyProposalPartnershipSuggestion')),
            ],
            bases=('partnership.moneypartnership',),
        ),
        migrations.CreateModel(
            name='MoneyRequestPartnership',
            fields=[
                ('moneypartnership_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='partnership.MoneyPartnership')),
                ('request', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='lending.MoneyRequestAd')),
                ('suggestion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='partnership.MoneyRequestPartnershipSuggestion')),
            ],
            bases=('partnership.moneypartnership',),
        ),
        migrations.AddField(
            model_name='moneytransaction',
            name='money_partnership',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partnership.MoneyPartnership'),
        ),
        migrations.AddField(
            model_name='moneytransaction',
            name='source_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='moneytransaction',
            name='target_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='moneypartnership',
            name='borrower',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrower', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='moneypartnership',
            name='creditor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creditor', to=settings.AUTH_USER_MODEL),
        ),
    ]
