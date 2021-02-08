from django.db import models
from P2PLending.users.models import User


class Review(models.Model):
    reviewed_user = models.ForeignKey(User, related_name='reviewed_user')
    author = models.ForeignKey(User, related_name='reviewer')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
