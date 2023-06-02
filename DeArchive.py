import os
import zipfile
import rarfile

def unarchive_comic(filename):
    file_extension = os.path.splitext(filename)[1].lower()

    if file_extension == '.cbz':
        with zipfile.ZipFile(filename, 'r') as zip_ref:
            zip_ref.extractall()
        print(f'Successfully unarchived {filename} using Zip.')
    elif file_extension == '.cbr':
        with rarfile.RarFile(filename, 'r') as rar_ref:
            rar_ref.extractall()
        print(f'Successfully unarchived {filename} using RAR.')
    else:
        print(f'Unsupported file extension: {file_extension}')

# Example usage
filename = 'example.cbz'
unarchive_comic(filename)
