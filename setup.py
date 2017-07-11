from setuptools import setup, find_packages

author_name = "Dmitry Orlov"
author_email = 'me@mosquito.su'


setup(
    name='pyword-stat',
    version='0.1',
    author='%s <%s>' % (author_name, author_email),
    author_email=author_email,
    license="MIT",
    description="pyWord-Stat simple text statistic tool",
    platforms="all",
    classifiers=[
        'Environment :: Console',
        'Programming Language :: Python :: 3 :: Only',
    ],
    packages=find_packages(exclude=['tests']),
    entry_points={
        'console_scripts': [
            'pyword-stat = pyword_stat:main',
        ]
    }
)