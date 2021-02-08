# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from djmoney.models.fields import MoneyField
from djmoney.models.managers import money_manager
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from P2PLending.users.exceptions import UserMoneyException
from P2PLending.users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    HOME_OWNERSHIP = (("own", "собственность"), ("rnt", "съемное жилье"), ("mrtg", "ипотека (кредит)"))
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    patronymic = models.CharField(_('patronymic'), max_length=30)
    phone = models.CharField(_('phone'), max_length=30)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    home_ownership = models.CharField(max_length=4,
                                      choices=HOME_OWNERSHIP,
                                      default="own")
    income = MoneyField(max_digits=10, decimal_places=2, default=0)

    objects = money_manager(UserManager())

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = "{} {} {}".format(self.last_name, self.first_name, self.patronymic)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def create_balance(self):
        return UserMoney.objects.create(user=self)

    def __str__(self):
        return self.get_full_name()


class UserMoney(models.Model):
    user = models.OneToOneField(User)
    balance = MoneyField(max_digits=10, decimal_places=2, default=0)

    def withdraw_money(self, amount):
        if self.balance < amount:
            raise UserMoneyException("Not enough money to withdraw")
        else:
            self.balance -= amount
            self.save()

    def put_money(self, amount):
        self.balance += amount
        self.save()

    @classmethod
    def has_money(cls, user, amount):
        user_balance = UserMoney.objects.get(user=user).balance
        return user_balance >= amount
