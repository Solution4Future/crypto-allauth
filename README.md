# Welcome to crypto-allauth

[![Build Status](https://travis-ci.org/Solution4Future/crypto-allauth.svg?branch=master)](https://travis-ci.org/Solution4Future/crypto-allauth)
[![Requirements Status](https://requires.io/github/Solution4Future/crypto-allauth/requirements.svg?branch=master)](https://requires.io/github/Solution4Future/crypto-allauth/requirements/?branch=master)
[![Shield Status](https://img.shields.io/pypi/v/crypto-allauth.svg)](https://pypi.python.org/pypi/crypto-allauth)
[![Join the chat at https://gitter.im/solution4future/crypto-allauth](https://badges.gitter.im/solution4future/crypto-allauth.svg)](https://gitter.im/solution4future/crypto-allauth?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

(DISCLAIMER! This software is early alpha and doesn't have tests yet so you are using it on your own)

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

## Roadmap

- U2F support (Yubikey and others)
- Offline Trezor support
- Keybase support

## Final notes

Feel free to create pull requests.

If you feel generous you can donate: [1AnrshDKmzRU57GTNJ2ki1bTKK45NDd2Dn](http://i.imgur.com/hlhWwOO.png)
