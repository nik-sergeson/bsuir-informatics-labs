from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='income',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0'), max_digits=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='income_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('BYN', 'Belarussian Ruble')], default='BYN', editable=False, max_length=3),
        ),
        migrations.AlterField(
            model_name='usermoney',
            name='balance_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('BYN', 'Belarussian Ruble')], default='BYN', editable=False, max_length=3),
        ),
    ]
