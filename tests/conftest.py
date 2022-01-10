import os
import shutil
import pytest


def _get_nested_folderpath(num_layers, root_folder='tmp'):
    return os.path.join(
        root_folder, *[f'folder_{i:02d}' for i in range(num_layers)])


@pytest.fixture(scope="session")
def generated_folderpath(num_layers=3, extensions=['txt', 'py', 'md']):
    # Create folder structure
    folderpath = os.path.join(
        _get_nested_folderpath(num_layers))
    os.makedirs(folderpath, exist_ok=True)
    
    # Create files
    for i in range(num_layers + 1):
        folderpath = _get_nested_folderpath(i)
        for extension in extensions:
            filepath = os.path.join(folderpath, f"file.{extension}")
            with open(filepath, 'w') as f:
                f.write("sample text")
            
            # Make read only
            #os.chmod(filepath, 0o400)

    # Create hidden file
    with open("tmp/.env", "w") as f:
        f.write("SECRET_KEY=1234")
    
    # Add symbolic link
    os.mkdir("tmp/f")
    os.symlink("f", "tmp/link_f", target_is_directory=True)
    # Add broken symbolic link
    os.symlink("tmp/f", "tmp/dead_link_f", target_is_directory=True)

    yield "tmp"
    
    # Remove folder structure
    shutil.rmtree("tmp")
