from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('lending', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('similarity', models.FloatField()),
            ],
        ),
        migrations.AlterField(
            model_name='moneyproposalad',
            name='max_amount_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('BYN', 'Belarussian Ruble')], default='BYN', editable=False, max_length=3),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='proposal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lending.MoneyProposalAd'),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lending.MoneyRequestAd'),
        ),
    ]
