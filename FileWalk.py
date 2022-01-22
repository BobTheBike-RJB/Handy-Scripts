## This module helps to generate a full list of files within a directory and its sub-directories.
## - Two key functions of this module are 1) returning the full path to the file and 2) only returning the requested file types.
## 
## Accepts two arguments: source_directory, ext_list
## then it checks to see which files found in the walk of the source folder match the file type.
## Response is given as a dictionary containing: file_count, folder_count, and file_list

import os

def walk(source_dir, ext_list):
    ##1) Variables for returning metrics
    file_count = 0
    folder_count = 0
    file_list = []
    response_dict = {}

    ##2) Loop for walking folders and identifying files that meet criteria 
    for subdir, dirs, files in os.walk(source_dir):
        for file in files:
            file_name, file_extension = os.path.splitext(file)

            ##Only run on file types
            if file_extension.lower() in ext_list:
                file_count += 1
                file_list.append(os.path.join(subdir,file))
        
        for dir in dirs:
            folder_count += 1 

    response_dict["file_count"] = file_count
    response_dict["folder_count"] = folder_count
    response_dict["file_list"] = file_list    
    return response_dict