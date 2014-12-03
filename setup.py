import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    ]

setup(name='pypkpass',
      version='0.0',
      description='A series of Python objects for the construction, management, and serialization of iOS PassKit passes',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Application",
        ],
      author='Patrick Perini',
      author_email='pcperini@gmail.com',
      url='https://github.com/pcperini',
      keywords='web ios pkpass',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='PyPKPass',
      install_requires=requires,
      )
