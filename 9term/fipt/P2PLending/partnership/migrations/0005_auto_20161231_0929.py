from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnership', '0004_auto_20161230_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moneyproposalpartnershipsuggestion',
            name='status',
            field=models.CharField(choices=[('SUG', 'Suggested'), ('ACC', 'Accepted'), ('REJ', 'Rejected'), ('CAN', 'Cancelled')], default='SUG', max_length=3),
        ),
        migrations.AlterField(
            model_name='moneyrequestpartnershipsuggestion',
            name='status',
            field=models.CharField(choices=[('SUG', 'Suggested'), ('ACC', 'Accepted'), ('REJ', 'Rejected'), ('CAN', 'Cancelled')], default='SUG', max_length=3),
        ),
    ]
