# folderstats

[![](https://img.shields.io/pypi/v/folderstats.svg)](https://pypi.python.org/pypi/folderstats)

This is a python module and command-line interface that creates statistics from a folder structure. It returns a [Pandas](http://pandas.pydata.org/) dataframe from the folders and files from a selected folder.

![Folder Structure Graph](folder_structure.png)

# Installation

```bash
pip install folderstats
```

# Usage

To get statistics of a folder structure as a Pandas dataframe in Python you can type:

```python
import folderstats  
df = folderstats.folderstats(
    '.', hash_name='md5',
    exclude=["tests", "venv", "__pycache__"],
    ignore_hidden=True)
df
```

| path | name | extension | size | atime | mtime | ctime | folder | num_files | depth | uid | md5 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ./folder_structure.png | folder_structure | png | 525239 | 2022-01-10 16:08:32 | 2020-11-22 19:38:03 | 2020-11-22 19:38:03 | False |     | 0   | 1000 | a3cac43de8dd5fc33d7bede1bb1849de |
| ./requirements.txt | requirements | txt | 14  | 2022-01-10 18:37:52 | 2022-01-08 17:29:52 | 2022-01-08 17:29:52 | False |     | 0   | 1000 | d8e272adf08f0389ef08be879d851df8 |
| ./requirements-dev.txt | requirements-dev | txt | 33  | 2022-01-10 14:14:50 | 2022-01-08 17:54:50 | 2022-01-08 17:54:50 | False |     | 0   | 1000 | 42c7e7d9bc4620c2c7a12e6bbf8120bb |
| ./README.md | README | md  | 3909 | 2022-01-10 18:37:52 | 2022-01-10 18:37:34 | 2022-01-10 18:37:34 | False |     | 0   | 1000 | 4339e186a35d77689419e996ee3998dc |
| ./folderstats/\_\_main\_\_.py | \_\_main\_\_ | py  | 3313 | 2022-01-10 18:06:03 | 2022-01-10 18:05:58 | 2022-01-10 18:05:58 | False |     | 1   | 1000 | 62652872e08be115495aaf6e9f3a239a |
| ./folderstats/\_\_init\_\_.py | \_\_init\_\_ | py  | 4556 | 2022-01-10 18:05:12 | 2022-01-10 18:04:56 | 2022-01-10 18:04:56 | False |     | 1   | 1000 | f0c8eb98713ddec7a4812a1471384296 |
| ./folderstats | folderstats |     | 7869 | 2022-01-10 17:10:15 | 2022-01-10 17:10:15 | 2022-01-10 17:10:15 | True | 2.0 | 1   | 1000 |     |
| ./LICENSE | LICENSE |     | 1073 | 2022-01-10 16:08:38 | 2020-11-22 19:38:03 | 2020-11-22 19:38:03 | False |     | 0   | 1000 | 1232cbd9eced47e27816f69740ad479d |
| ./setup.py | setup | py  | 1925 | 2022-01-10 16:29:32 | 2020-11-22 19:38:03 | 2020-11-22 19:38:03 | False |     | 0   | 1000 | 01d39c60a0b41e6c928a6d3df6085d63 |
| .   | .   |     | 544158 | 2022-01-10 18:37:00 | 2022-01-10 18:37:00 | 2022-01-10 18:37:00 | True | 8.0 | 0   | 1000 |     |

You can use the same functionality as a command-line interface which can generate files (CSV or JSON) or print the statistics directly into the command line:

```bash
folderstats . -c md5 -i -o stats.csv
```

In order to see the other available arguments, type:

```bash
folderstats --help
```

```
usage: folderstats [-h] [-o OUTPUT_FILEPATH] [-c HASH_NAME] [-a] [-m] [-i]
                   [-p] [-e EXCLUDE] [-f FILTER_EXTENSION] [-l] [-v]
                   folderpath

Creates statistics from a folder structure

positional arguments:
  folderpath            input folder path

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT_FILEPATH    output filepath, CSV and JSON supported
  -c HASH_NAME          hash function for checksum
  -a                    add absolute path column
  -m                    store timestamps with microseconds
  -i                    ignore hidden files and folders, Linux and Unix only
  -p                    Add index and parent index
  -e EXCLUDE, --exclude EXCLUDE
                        Exclude files and folders by name
  -f FILTER_EXTENSION, --filter-extension FILTER_EXTENSION
                        Filter files by extension
  -l, --follow-links    Follow symbolic and hard links
  -v                    verbose console output
```

# Testing

Prepare dev environment with:

```bash
# Create virtual environement
python -m venv ./venv

# Install dependencies
pip install -r requirements-dev.txt
pip install -r requirements.txt

# Activate virtual environment
source venv/bin/activate
```

To run unit tests, type:

```bash
pytest -v
```

# License

This project is licensed under the MIT license. See the [LICENSE](LICENSE) for details.
