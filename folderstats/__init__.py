__version__ = "0.4.0"

import os
import stat
import hashlib
import pandas as pd
from datetime import datetime


def calculate_hash(filepath, hash_name):
    """Calculate the hash of a file. The available hashes are given by the hashlib module. The available hashes can be listed with hashlib.algorithms_available."""

    hash_name = hash_name.lower()
    if not hasattr(hashlib, hash_name):
        raise Exception('Hash algorithm not available : {}'\
            .format(hash_name))

    with open(filepath, 'rb') as f:
        checksum = getattr(hashlib, hash_name)()
        for chunk in iter(lambda: f.read(4096), b''):
            checksum.update(chunk)

        return checksum.hexdigest()


def _recursive_folderstats(
    root_entry,
    items=None,
    hash_name=None,
    ignore_hidden=False,
    exclude=None,
    filter_extension=None,
    follow_links=False,
    depth=0,
    idx=1,
    parent_idx=0,
    verbose=False
):
    """Helper function that recursively collects folder statistics and returns current id, foldersize and number of files traversed."""
    items = items if items is not None else []
    foldersize, num_files = 0, 0
    current_idx = idx

    if isinstance(root_entry, os.DirEntry):
        folderpath = root_entry.path
        foldername = root_entry.name
        root_stat  = root_entry.stat()
    else:
        folderpath = root_entry
        foldername = os.path.basename(root_entry)
        root_stat  = os.stat(root_entry)

    if os.access(folderpath, os.R_OK):
        for entry in os.scandir(folderpath):
            if ignore_hidden and entry.name.startswith('.'):
                continue

            if exclude and (entry.name in exclude):
                continue

            idx += 1
            if entry.is_dir() or entry.is_symlink():
                if verbose:
                    print(f'FOLDER: {entry.path}')

                if entry.is_symlink():
                    # Check if symbolic link is broken
                    if not follow_links \
                       or os.path.exists(os.readlink(entry.path)):
                        continue
                
                stat = entry.stat()
                foldersize += stat.st_size

                idx, items, _foldersize, _num_files = _recursive_folderstats(
                    entry.path, items, hash_name,
                    ignore_hidden, exclude, filter_extension, follow_links,
                    depth + 1, idx, current_idx, verbose)
                foldersize += _foldersize
                num_files += _num_files
            else:
                filename, extension = os.path.splitext(entry.name)
                extension = extension[1:] if extension else None
                
                if filter_extension and (extension not in filter_extension):
                    continue

                stat = entry.stat()
                item = [
                    idx, entry.path, filename, extension, stat.st_size,
                    stat.st_atime, stat.st_mtime, stat.st_ctime,
                    False, None, depth, current_idx, stat.st_uid
                ]
                if hash_name:
                    if os.access(entry.path, os.R_OK):
                        item.append(calculate_hash(entry.path, hash_name))
                
                items.append(item)
                foldersize += stat.st_size
                num_files += 1

    item = [
        current_idx, folderpath, foldername, None, foldersize,
        root_stat.st_atime, root_stat.st_mtime, root_stat.st_ctime,
        True, num_files, depth, parent_idx, root_stat.st_uid
    ]
    if hash_name is not None:
        item.append(None)
    
    items.append(item)

    return idx, items, foldersize, num_files


def folderstats(
    folderpath,
    hash_name=None,
    microseconds=False,
    absolute_paths=False,
    exclude=None,
    filter_extension=None,
    follow_links=False,
    ignore_hidden=False,
    parent=True,
    verbose=False
):
    """Function that returns a Pandas dataframe from the folders and files from a selected folder."""
    columns = [
        'id', 'path', 'name', 'extension', 'size',
        'atime', 'mtime', 'ctime',
        'folder', 'num_files', 'depth', 'parent', 'uid'
    ]
    if hash_name:
        hash_name = hash_name.lower()
        columns.append(hash_name)

    idx, items, foldersize, num_files = _recursive_folderstats(
        folderpath,
        hash_name=hash_name,
        ignore_hidden=ignore_hidden,
        exclude=exclude,
        filter_extension=filter_extension,
        follow_links=follow_links,
        verbose=verbose)
    df = pd.DataFrame(items, columns=columns)

    for col in ['atime', 'mtime', 'ctime']:
        df[col] = df[col].apply(
            lambda d: datetime.fromtimestamp(d) if microseconds else \
                datetime.fromtimestamp(d).replace(microsecond=0))

    if absolute_paths:
        df.insert(1, 'absolute_path', df['path'].apply(
            lambda p: os.path.abspath(p)))

    if not parent:
        df.drop(columns=['id', 'parent'], inplace=True)

    return df
