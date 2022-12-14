import re
from setuptools import setup


with open('README.md', encoding='utf-8') as fp:
    readme = fp.read()

with open('requirements.txt') as fp:
    requirements = fp.readlines()

with open('pokedex/__init__.py') as fp:
    contents = fp.read()

    try:
        version = re.search(
            r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', contents, re.M
        ).group(1)
    except AttributeError:
        raise RuntimeError('Could not identify version') from None

    try:
        author = re.search(
            r'^__author__\s*=\s*[\'"]([^\'"]*)[\'"]', contents, re.M
        ).group(1)
    except AttributeError:
        author = 'Harshit Mannava'


setup(
    name='pokedex',
    author=author,
    url='https://github.com/Futureslinky/pokedex',
    project_urls={
        "Issue tracker": "https://github.com/Futureslinky/pokedex/issues",
        
    },
    version=version,
    packages=['pokedex'],
    license='GNU General Public License v3.0',
    description="A python wrapper to bring pokédex data into python.",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=requirements,
    extras_require={
        'requests': ['requests']
    },
    python_requires='>=3.8.0',
    classifiers=[
        'License :: GNU General Public License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ]
)
