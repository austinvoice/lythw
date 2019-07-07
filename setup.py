# setup file -- needs to have customization for specific project

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Brian Goffman',
    'url': 'URL to get it',
    'download_url', 'Where to download it',
    'author_email': 'brian.goffman@gmail.com',
    'version', '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts', [],
    'name', 'projectname'
}

setup(**config)
