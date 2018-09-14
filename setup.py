import setuptools
from setuptools import setup

setup(name='regex-file-collector',
      version='0.1',
      description='Tool read file-paths obeying a regex pattern.',
      url='http://github.com/henriasv/regex-file-collector',
      author='Henrik Andersen Sveinsson',
      author_email='henrik.sveinsson@me.com',
      license='GNU GPL v3.0',
      packages=setuptools.find_packages(),
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)