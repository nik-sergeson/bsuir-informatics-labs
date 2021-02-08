from __future__ import unicode_literals

from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('lending', '0002_auto_20161203_0618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moneyproposalad',
            name='min_amount_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('BYN', 'Belarussian Ruble')], default='BYN', editable=False, max_length=3),
        ),
        migrations.AlterField(
            model_name='moneyrequestad',
            name='amount_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('BYN', 'Belarussian Ruble')], default='BYN', editable=False, max_length=3),
        ),
    ]
