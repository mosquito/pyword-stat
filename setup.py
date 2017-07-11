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
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    packages=find_packages(exclude=['tests']),
)