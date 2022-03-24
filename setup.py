try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = ''

setup(
    long_description=readme,
    name='pokemon-battle-cli',
    version='0.0.1',
    description='pokemon battle cli',
    python_requires='==3.*,>=3.7.0',
    author='Raphael Vieira Rossi',
    author_email='raphael.vieira.rossi@gmail.com',
    license='MIT',
    entry_points={"console_scripts": ["pokemon-battle=pokemon_battle_cli.cli:main"]},
    packages=[
        'pokemon_battle_cli',
    ],
    package_dir={"": "."},
    package_data={
    },
    install_requires=[
    ],
    extras_require={
        "dev": [
        ]
    },
)

