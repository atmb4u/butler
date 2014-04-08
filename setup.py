from setuptools import setup
from butler import __version__
setup(name='python-butler',
      version=__version__,
      description='Python Dictionaries and Lists on Steroids',
      url='http://github.com/atmb4u/butler',
      author='Anoop Thomas Mathew',
      author_email='atmb4u@gmail.com',
      license='BSD',
      packages=['butler'],
      zip_safe=False)
