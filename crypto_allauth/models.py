from __future__ import absolute_import

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class CryptoApp(models.Model):
    name = models.CharField(_('name'), max_length=40)
