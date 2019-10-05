from django.contrib.auth.models import AbstractUser
from django.db import models

from main.models import Company


class User(AbstractUser):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    address = models.TextField(blank=True, null=False)
    birth_date = models.DateField(blank=True, null=True)

    designation_choices = [
        (1, 'Developer', ),
        (2, 'Sales Manager', ),
        (3, 'Analyst', ),
        (4, 'Operations', ),
        (5, 'Account Manager')
    ]
    designation = models.PositiveSmallIntegerField(choices=designation_choices, default='1')

    class Meta:
        db_table = 'user'
