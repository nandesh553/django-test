from django.db import models
from django.utils.translation import gettext as _


class Company(models.Model):
    name = models.CharField(max_length=100, help_text=_('Company Name'))
    address = models.TextField(blank=True, null=False, help_text=_('Company Address'))
    company_type = models.CharField(max_length=250, blank=True, null=False, help_text=_('Company Type'))

    class Meta:
        db_table = 'company'

    def __str__(self):
        return self.name.title()

    def __repr__(self):
        return self.name.title()
