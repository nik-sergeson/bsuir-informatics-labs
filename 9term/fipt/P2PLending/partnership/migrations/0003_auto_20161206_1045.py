from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('lending', '0003_auto_20161206_1045'),
        ('partnership', '0002_auto_20161203_0618'),
    ]

    operations = [
        migrations.AddField(
            model_name='moneyproposalpartnershipsuggestion',
            name='from_request',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lending.MoneyRequestAd'),
        ),
        migrations.AddField(
            model_name='moneyrequestpartnershipsuggestion',
            name='from_proposal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lending.MoneyProposalAd'),
        ),
        migrations.AlterField(
            model_name='moneyproposalpartnershipsuggestion',
            name='amount_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('BYN', 'Belarussian Ruble')], default='BYN', editable=False, max_length=3),
        ),
        migrations.AlterField(
            model_name='moneytransaction',
            name='amount_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('BYN', 'Belarussian Ruble')], default='BYN', editable=False, max_length=3),
        ),
    ]
