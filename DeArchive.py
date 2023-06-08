import os
from zipfile import ZipFile
from rarfile import RarFile
from tarfile import TarFile
from ReadYAMLProperties import Configuration

def unarchive_comic(filename):

    config = Configuration()
    config.read_config()
    outputdir = config.get_property("tempdirStr")
    print(f"Outputdir: {outputdir}")

    file_extension = os.path.splitext(filename)[1].lower()
    # Need to fix this
    # comicdir = os.path.split(filename)[1].lower()
    # call appropriate extractor depending on filetype of archive
    if file_extension == '.cbz':
        with ZipFile(filename, 'r') as zip_ref:
            zip_ref.extractall(outputdir)
        print(f'Successfully unarchived {filename} using Zip.')
    
    elif file_extension == '.cbr':
        with RarFile(filename, 'r') as rar_ref:
            rar_ref.extractall(outputdir)
        print(f'Successfully unarchived {filename} using RAR.')
    
    elif file_extension == 'cbt':
        with TarFile(filename, r) as tar_ref:
            tar_ref.extractall(outputdir)
        print(f'Successfully unarchived {filename} using TAR.')
    else:
        print(f'Unsupported file extension: {file_extension}')

# Example usage
filename = '../data/AlphaFlight-078.cbz'
unarchive_comic(filename)
