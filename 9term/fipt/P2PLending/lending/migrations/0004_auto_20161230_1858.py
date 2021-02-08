from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lending', '0003_auto_20161206_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='moneyproposalad',
            name='status',
            field=models.CharField(choices=[('OPN', 'Opened'), ('CLS', 'Closed')], default='OPN', max_length=3),
        ),
        migrations.AddField(
            model_name='moneyrequestad',
            name='status',
            field=models.CharField(choices=[('OPN', 'Opened'), ('CLS', 'Closed')], default='OPN', max_length=3),
        ),
    ]
