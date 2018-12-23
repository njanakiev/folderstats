folderstats
===========

.. image:: https://img.shields.io/pypi/v/folderstats.svg
        :target: https://pypi.python.org/pypi/folderstats

This is a python module and command-line interface that creates statistics from a folder structure. It returns a [Pandas](http://pandas.pydata.org/) dataframe from the folders and files from a selected folder.

Installation
------------

.. code-block:: bash

	pip install folderstats


Usage
-----

To get statistics of a folder structure as a Pandas dataframe you can type:

.. code-block:: python

	import folderstats  
	df = folderstats.folderstats('.', hash_name='md5', ignore_hidden=True)
	df

+-----------+------+---+---+-------+-------+-------+---+---+------------+
| path      | name | e | s | atime | mtime | ctime | f | n | md5        |
|           |      | x | i |       |       |       | o | u |            |
|           |      | t | z |       |       |       | l | m |            |
|           |      | e | e |       |       |       | d | _ |            |
|           |      | n |   |       |       |       | e | f |            |
|           |      | s |   |       |       |       | r | i |            |
|           |      | i |   |       |       |       |   | l |            |
|           |      | o |   |       |       |       |   | e |            |
|           |      | n |   |       |       |       |   | s |            |
+===========+======+===+===+=======+=======+=======+===+===+============+
| ./folders | \__m | p | 2 | 2018- | 2018- | 2018- | F |   | 87446d672b |
| tats/__ma | ain_ | y | 5 | 12-23 | 12-23 | 12-23 | a |   | 598eda1716 |
| in__.py   | \_   |   | 9 | 23:14 | 23:14 | 23:14 | l |   | 1296ea333e |
|           |      |   | 6 | :23   | :22   | :22   | s |   | cc         |
|           |      |   |   |       |       |       | e |   |            |
+-----------+------+---+---+-------+-------+-------+---+---+------------+
| ./folders | \__i | p | 2 | 2018- | 2018- | 2018- | F |   | 7b4adc532f |
| tats/__in | nit_ | y | 7 | 12-23 | 12-23 | 12-23 | a |   | 304863423e |
| it__.py   | \_   |   | 9 | 23:09 | 23:09 | 23:09 | l |   | c11afd3232 |
|           |      |   | 0 | :07   | :05   | :05   | s |   | ad         |
|           |      |   |   |       |       |       | e |   |            |
+-----------+------+---+---+-------+-------+-------+---+---+------------+
| ./folders | ./fo |   | 1 | 2018- | 2018- | 2018- | T | 5 |            |
| tats      | lder |   | 3 | 12-23 | 12-23 | 12-23 | r | . |            |
|           | stat |   | 8 | 23:14 | 23:14 | 23:14 | u | 0 |            |
|           | s    |   | 0 | :48   | :48   | :48   | e |   |            |
|           |      |   | 2 |       |       |       |   |   |            |
+-----------+------+---+---+-------+-------+-------+---+---+------------+
| ./README. | READ | m | 7 | 2018- | 2018- | 2018- | F |   | 747a23dbc0 |
| md        | ME   | d | 6 | 12-23 | 12-22 | 12-22 | a |   | 6da98570c5 |
|           |      |   |   | 22:17 | 14:50 | 14:50 | l |   | 0edaa3527a |
|           |      |   |   | :25   | :43   | :43   | s |   | b3         |
|           |      |   |   |       |       |       | e |   |            |
+-----------+------+---+---+-------+-------+-------+---+---+------------+
| ./LICENSE | LICE |   | 1 | 2018- | 2018- | 2018- | F |   | 1232cbd9ec |
|           | NSE  |   | 0 | 12-23 | 12-22 | 12-22 | a |   | ed47e27816 |
|           |      |   | 7 | 22:34 | 14:50 | 14:50 | l |   | f69740ad47 |
|           |      |   | 3 | :16   | :43   | :43   | s |   | 9d         |
|           |      |   |   |       |       |       | e |   |            |
+-----------+------+---+---+-------+-------+-------+---+---+------------+
| ./setup.p | setu | p | 1 | 2018- | 2018- | 2018- | F |   | b5410458c1 |
| y         | p    | y | 9 | 12-23 | 12-23 | 12-23 | a |   | 334a753c4d |
|           |      |   | 7 | 22:50 | 22:50 | 22:50 | l |   | d71db0f337 |
|           |      |   | 5 | :10   | :09   | :09   | s |   | d2         |
|           |      |   |   |       |       |       | e |   |            |
+-----------+------+---+---+-------+-------+-------+---+---+------------+
| .         | .    |   | 2 | 2018- | 2018- | 2018- | T | 8 |            |
|           |      |   | 1 | 12-23 | 12-23 | 12-23 | r | . |            |
|           |      |   | 0 | 23:16 | 23:16 | 23:16 | u | 0 |            |
|           |      |   | 2 | :26   | :26   | :26   | e |   |            |
|           |      |   | 2 |       |       |       |   |   |            |
+-----------+------+---+---+-------+-------+-------+---+---+------------+


You can use the same functionality as a command-line interface which can generate files (CSV or JSON) or print the statistics directly into the command line:

.. code-block:: bash

	folderstats . -c md5 -i -o stats.csv


In order to see the other available arguments type:

.. code-block:: bash

	folderstats --help


License 
-------

This project is licensed under the MIT license. See the [LICENSE](LICENSE) for details.
