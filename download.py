from office365_sharepoint import Sharepoint
import re
import sys, os
from pathlib import PurePath

# SHAREPOINT FOLDER NAME, from where to download
FOLDER_NAME = sys.argv[1]
# LOCAL DESTINATION FOLDER to Save the files
FOLDER_DEST = sys.argv[2]
# Specific file name to be downloaded from sharepoint
FILE_NAME = sys.argv[3]


def save_file(file_n, file_obj):
    file_dir_path = PurePath(FOLDER_DEST, file_n)
    with open(file_dir_path, 'wb') as f:
        f.write(file_obj)


def get_file(file_n, folder):
    file_obj = Sharepoint().download_file(file_n, folder)
    save_file(file_n, file_obj)


def get_files(folder):
    files_list = Sharepoint()._get_files_list(folder)
    for file in files_list:
        get_file(file.name, folder)


if __name__ == '__main__':
    if FILE_NAME != 'None':
        get_file(FILE_NAME, FOLDER_NAME)
    else:
        get_files(FOLDER_NAME)
