# Welcome to crypto-allauth

Crypto-allauth is a library that adds support for some advanced login methods.
It was first drafted at the TREZOR 2 Hackathon in Prague.

Right now you can only use Trezor but plans are to support other hardware encryption solutions.

## Installation

```sh
$ pip install crypto-allauth
```

```py
INSTALLED_APPS = {
        ...
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        ...
        'crypto_allauth.providers.trezor',
        ...
}

```

And you're all set up.

For the "Login with TREZOR" button to work properly you either need a Chrome plugin or a trezor-bridge daemon. Go to [satoshilabs.com/trezor](http://satoshilabs.com/trezor/) to learn more.

