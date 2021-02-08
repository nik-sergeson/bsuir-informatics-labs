from __future__ import unicode_literals

from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('partnership', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moneypartnership',
            name='annuity_payment_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('BYN', 'Belarussian Ruble')], default='BYN', editable=False, max_length=3),
        ),
        migrations.AlterField(
            model_name='moneypartnership',
            name='dept_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('BYN', 'Belarussian Ruble')], default='BYN', editable=False, max_length=3),
        ),
    ]
