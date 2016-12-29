try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'NAME',
    'author': 'Andrew Philpot',
    'url': 'http://www.isi.edu',
    'download_url': 'http://www.isi.edu',
    'author_email': 'philpot@isi.edu',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'NAME'
}

setup(**config)
