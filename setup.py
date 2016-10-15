#!/usr/bin/env python
import io
import os
import sys
from fnmatch import fnmatchcase

from setuptools import setup, find_packages
from distutils.util import convert_path

# Provided as an attribute, so you can append to these instead
# of replicating them:
standard_exclude = ["*.py", "*.pyc", "*~", ".*", "*.bak", "Makefile"]
standard_exclude_directories = [
    ".*", "CVS", "_darcs", "./build",
    "./dist", "EGG-INFO", "*.egg-info",
    "./example"
]

# Copied from paste/util/finddata.py
def find_package_data(where=".", package="", exclude=standard_exclude,
                      exclude_directories=standard_exclude_directories,
                      only_in_packages=True, show_ignored=False):
    """
    Return a dictionary suitable for use in ``package_data``
    in a distutils ``setup.py`` file.
    The dictionary looks like::
        {"package": [files]}
    Where ``files`` is a list of all the files in that package that
    don't match anything in ``exclude``.
    If ``only_in_packages`` is true, then top-level directories that
    are not packages won't be included (but directories under packages
    will).
    Directories matching any pattern in ``exclude_directories`` will
    be ignored; by default directories with leading ``.``, ``CVS``,
    and ``_darcs`` will be ignored.
    If ``show_ignored`` is true, then all the files that aren't
    included in package data are shown on stderr (for debugging
    purposes).
    Note patterns use wildcards, or can be exact paths (including
    leading ``./``), and all searching is case-insensitive.
    """

    out = {}
    stack = [(convert_path(where), "", package, only_in_packages)]
    while stack:
        where, prefix, package, only_in_packages = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                            or fn.lower() == pattern.lower()):
                        bad_name = True
                        if show_ignored:
                            print >> sys.stderr, (
                                "Directory %s ignored by pattern %s"
                                % (fn, pattern))
                        break
                if bad_name:
                    continue
                if (os.path.isfile(os.path.join(fn, "__init__.py"))
                        and not prefix):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + "." + name
                    stack.append((fn, "", new_package, False))
                else:
                    stack.append((fn, prefix + name + "/", package,
                                  only_in_packages))
            elif package or not only_in_packages:
                # is a file
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                            or fn.lower() == pattern.lower()):
                        bad_name = True
                        if show_ignored:
                            print >> sys.stderr, (
                                "File %s ignored by pattern %s"
                                % (fn, pattern))
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out


excluded_directories = standard_exclude_directories

package_data = find_package_data(exclude_directories=excluded_directories)

long_description = io.open('README.md', encoding='utf-8').read()

METADATA = dict(
    name='crypto-allauth',
    version='0.0.5',
    include_package_data=True,
    long_description=long_description,
    url='https://github.com/Solution4Future/crypto-allauth',
    license='MIT',
    author='Dominik Kozaczko',
    author_email='dominik.kozaczko@solution4future.com',
    description='Plugin for django-allauth that allows authentication using cryptographic tools like Trezor.',
    install_requires=['bitcoin>=1.1.42', 'django-allauth>=0.27.0'],
    zip_safe=False,

    keywords='django auth account trezor registration',
    classifiers=[
        # 'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Environment :: Web Environment',
        'Topic :: Internet',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Framework :: Django',
    ],
    packages=find_packages(exclude=['example']),
    package_data=package_data,
)

if __name__ == '__main__':
    setup(**METADATA)
