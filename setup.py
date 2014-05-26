#!/usr/bin/env python
from distutils.core import setup
import neonsms


setup(name='neonsms',
      version=neonsms.__version__,
      description="Twilio compatible shim for neonsms API",
      long_description="A Twilio API compatible wrapper for neonsms.ie",
      author=neonsms.__author__,
      author_email='jonathan@jonharrington.org',
      url='https://github.com/prio/neonsms',
      download_url='https://github.com/prio/neonsms',
      license=neonsms.__license__,
      platforms=['all'],
      classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
      ],
      py_modules=['neonsms', 'neonsms.rest'],
      )
