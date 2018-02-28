#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created by dorayo@2017.4.21
'''
批量重命名文件夹下的文件
'''

import os
import sys
import argparse

def batch_rename(work_dir, old_ext, new_ext):
    '''
    This will batch rename a group of files in a given directory,
    once you pass the current and new extensions
    '''
    for filename in os.listdir(work_dir):
        # Get the file extension
        file_ext = os.path.splitext(filename)[1]
        # Start of the logic to check the file extensions, if old_ext == file_ext
        if file_ext == old_ext:
            # Returns changed name of the file with new extension
            basefilename = filename.split('.')[0]
            newname = basefilename+new_ext
            # Rename
            os.rename(
                os.path.join(work_dir, filename),
                os.path.join(work_dir, newname)
            )

def get_parser():
    parser = argparse.ArgumentParser(description='change extension of files in a working directory')
    parser.add_argument('work_dir', metavar='WORK_DIR', type=str, nargs=1, help='the directory where to change extension')
    parser.add_argument('old_ext', metavar='OLD_EXT', type=str, nargs=1, help='old extension')
    parser.add_argument('new_ext', metavar='NEW_EXT', type=str, nargs=1, help='new extension')
    return parser

def main():
    '''
    This will be called if the script is directly invoked.
    '''
    # adding command line argument
    parser = get_parser()
    args = vars(parser.parse_args())

    # Set the variable work_dir with the first argument passed
    work_dir = args['work_dir'][0]
    # Set the variable old_ext with the second argument passed
    old_ext = args['old_ext'][0]
    # Set the variable new_ext with the third argument passed
    new_ext = args['new_ext'][0]

    batch_rename(work_dir, old_ext, new_ext)

if __name__ == '__main__':
    main()
