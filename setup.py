from distutils.core import setup

setup(
    name='DiscordBot',
    version='0.1dev',

    description='Python 3.5+ Discord Bot for free game offers on Steam and Epic Games Store',

    # The project's main homepage.
    url='https://github.com/game-notify',

    # Author details.
    author='Kaspar Wetsch',
    author_email='kaspar.wetsch@gmx.de',

    # License
    license='MIT',

    # Classifiers
    classifiers=[
        # Project Stage:
        'Development Status :: 3 - Alpha',

        # Intended for:
        'Intended Audience :: Developers, Artists',
        'Topic :: Software Development :: Tools',

        # License:
        'License :: MIT',

        # Supported Python versions:
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
        'Programming Language :: Python :: 3.7'
        'Programming Language :: Python :: 3.8'

    ],

    # Keywords
    keywords='development tools chat bot',

    # Required dependencies. Will be installed by pip
    # when the project is installed.
    install_requires=['discord.py', 'requests'],
)
