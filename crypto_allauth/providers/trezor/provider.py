import hashlib
import json
import uuid

import datetime

from allauth.compat import render_to_string
from django.utils.safestring import mark_safe

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse
from django.core.urlresolvers import reverse
from django.utils.http import urlencode

from allauth.socialaccount import providers
from allauth.socialaccount.providers.base import Provider, ProviderAccount


class TrezorAccount(ProviderAccount):
    def get_brand(self):
        return "trezor"

    def to_str(self):
        return self.account.uid


class TrezorProvider(Provider):
    id = "trezor"
    name = "Trezor"
    account_class = TrezorAccount

    def extract_extra_data(self, data):
        return data

    def extract_uid(self, data):
        return data['public_key']

    def extract_common_fields(self, data):
        return {}

    # def media_js(self, request):
    #     def abs_uri(name):
    #         return request.build_absolute_uri(reverse(name))
    #
    #     trezor_data = {
    #         'challenge_hidden': hashlib.sha512(uuid.uuid4().bytes).hexdigest(),
    #         'challenge_visual': str(datetime.datetime.utcnow())
    #     }
    #
    #     ctx = {'trezor_data': trezor_data}
    #
    #     return render_to_string('trezor/trezor_connect.html', ctx, request=request)

    def get_login_url(self, request, next=None, **kwargs):
        return reverse("trezor_login")



providers.registry.register(TrezorProvider)
