from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnership', '0003_auto_20161206_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='moneypartnership',
            name='cancel_borrower_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='moneypartnership',
            name='cancel_creditor_approved',
            field=models.BooleanField(default=False),
        ),
    ]
