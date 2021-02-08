from __future__ import unicode_literals

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djmoney.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(max_length=30, verbose_name='last name')),
                ('patronymic', models.CharField(max_length=30, verbose_name='patronymic')),
                ('phone', models.CharField(max_length=30, verbose_name='phone')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('home_ownership', models.CharField(choices=[('own', 'own'), ('rnt', 'rent'), ('mrtg', 'mortgage')], default='own', max_length=4)),
                ('income_currency', djmoney.models.fields.CurrencyField(choices=[('BYR', 'Belarussian Ruble')], default='USD', editable=False, max_length=3)),
                ('income', djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0'), default_currency='USD', max_digits=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
        migrations.CreateModel(
            name='UserMoney',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance_currency', djmoney.models.fields.CurrencyField(choices=[('BYR', 'Belarussian Ruble')], default='BYR', editable=False, max_length=3)),
                ('balance', djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0'), max_digits=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
