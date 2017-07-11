pyword-stat
===========

The simple word counter.

Installation
------------

.. code-block:: shell

    pip install https://github.com/mosquito/pyword-stat/archive/master.zip


Usage example
-------------

.. code-block::

    $ echo "foo bar foo" | pyword-stat
    foo: 2
    bar: 1

Testing
-------

Just run make test (requires installed pytest)