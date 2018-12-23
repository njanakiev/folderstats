# folderstats

This is a python module and command-line interface that creates statistics from a folder structure. It returns a [Pandas](http://pandas.pydata.org/) dataframe from the folders and files from a selected folder.

# Installation

```bash
pip install folderstats
```

# Usage

To get statistics of a folder structure as a Pandas dataframe you can type:

```python
import folderstats  
df = folderstats.folderstats('.', hash_name='md5', ignore_hidden=True)
df
```

| path                          | name              | extension | size  | atime               | mtime               | ctime               | folder | num_files | md5                              | 
|-------------------------------|-------------------|-----------|-------|---------------------|---------------------|---------------------|--------|-----------|----------------------------------| 
| ./folderstats/\_\_main\_\_.py | \_\_main\_\_      | py        | 2596  | 2018-12-23 23:14:23 | 2018-12-23 23:14:22 | 2018-12-23 23:14:22 | False  |           | 87446d672b598eda17161296ea333ecc | 
| ./folderstats/\_\_init\_\_.py | \_\_init\_\_      | py        | 2790  | 2018-12-23 23:09:07 | 2018-12-23 23:09:05 | 2018-12-23 23:09:05 | False  |           | 7b4adc532f304863423ec11afd3232ad | 
| ./folderstats                 | ./folderstats     |           | 13802 | 2018-12-23 23:14:48 | 2018-12-23 23:14:48 | 2018-12-23 23:14:48 | True   | 5.0       |                                  | 
| ./README.md                   | README            | md        | 76    | 2018-12-23 22:17:25 | 2018-12-22 14:50:43 | 2018-12-22 14:50:43 | False  |           | 747a23dbc06da98570c50edaa3527ab3 | 
| ./LICENSE                     | LICENSE           |           | 1073  | 2018-12-23 22:34:16 | 2018-12-22 14:50:43 | 2018-12-22 14:50:43 | False  |           | 1232cbd9eced47e27816f69740ad479d | 
| ./setup.py                    | setup             | py        | 1975  | 2018-12-23 22:50:10 | 2018-12-23 22:50:09 | 2018-12-23 22:50:09 | False  |           | b5410458c1334a753c4dd71db0f337d2 | 
| .                             | .                 |           | 21022 | 2018-12-23 23:16:26 | 2018-12-23 23:16:26 | 2018-12-23 23:16:26 | True   | 8.0       |                                  | 



You can use the same functionality as a command-line interface which can generate files (CSV or JSON) or print the statistics directly into the command line:

```bash
folderstats . -c md5 -i -o stats.csv
```

In order to see the other available arguments type:

```bash
folderstats --help
```

# License 
This project is licensed under the MIT license. See the [LICENSE](LICENSE) for details.
