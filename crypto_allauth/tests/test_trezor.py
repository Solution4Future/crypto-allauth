from django.test import TestCase
from django.test.client import RequestFactory

from crypto_allauth.providers.trezor.provider import TrezorProvider


class TrezorProviderTest(TestCase):

    def test_trezor_account(self):
        request = RequestFactory()
        trezor_provider = TrezorProvider(request)
        self.assertEqual(trezor_provider.get_login_url(trezor_provider.request), '/trezor/login/')
