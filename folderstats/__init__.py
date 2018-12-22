__version__ = "0.1.0"

import os
import hashlib
import pandas as pd
from datetime import datetime


def calculate_hash(filepath, hash_name):
    hash_name = hash_name.lower()
    if not hasattr(hashlib, hash_name):
        raise Exception('Hash algorithm not available : {}'\
            .format(hash_name))

    with open(filepath, 'rb') as f:
        checksum = getattr(hashlib, hash_name)()
        for chunk in iter(lambda: f.read(4096), b''):
            checksum.update(chunk)
        return checksum.hexdigest()


def _recursive_folderstats(folderpath,
    items=[], hash_name=None, verbose=False):
    foldersize = 0
    for f in os.listdir(folderpath):
        filepath = os.path.join(folderpath, f)
        stats = os.stat(filepath)
        foldersize += stats.st_size

        if os.path.isdir(filepath):
            if verbose:
                print('FOLDER :', filepath)

            items, _foldersize = _recursive_folderstats(
                filepath, items, hash_name, verbose)
            foldersize += _foldersize
        else:
            item = [filepath, f, stats.st_size,
                    stats.st_atime, stats.st_mtime, stats.st_ctime, False]
            if hash_name:
                item.append(calculate_hash(filepath, hash_name))
            items.append(item)

    stats = os.stat(folderpath)
    item = [folderpath, folderpath, foldersize,
            stats.st_atime, stats.st_mtime, stats.st_ctime, True]
    if hash_name:
        item.append(None)
    items.append(item)

    return items, foldersize


def folderstats(folderpath, hash_name=None, verbose=False, microseconds=False):
    columns = ['path', 'name', 'size',
               'atime', 'mtime', 'ctime', 'folder']
    if hash_name:
        hash_name = hash_name.lower()
        columns.append(hash_name)

    items, foldersize = _recursive_folderstats(
        folderpath, hash_name=hash_name, verbose=verbose)
    df = pd.DataFrame(items, columns=columns)

    for col in ['atime', 'mtime', 'ctime']:
        df[col] = df[col].apply(
            lambda d: datetime.fromtimestamp(d) if microseconds else \
                datetime.fromtimestamp(d).replace(microsecond=0))

    return df
