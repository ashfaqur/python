import argparse
import os
import shutil
from os.path import exists


def main(origin_dir, dest_dir, db_dir):
    for file in os.listdir(origin_dir):
        if file.endswith('mp4'):
            full_path = origin_dir + file
            print(f'Full Path f{full_path}')
            if exists(dest_dir + file):
                print(f'"{file}" already copied to "{dest_dir}"')
                continue
            shutil.copy2(full_path, dest_dir)
            print(f'"{file}" copied to "{dest_dir}"')
        else:
            continue


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script for moving videos')
    parser.add_argument('origin_dir', metavar='origin_dir',
                        type=str, help='origin video dir')
    parser.add_argument('dest_dir', metavar='dest_dir',
                        type=str, help='destination directory')
    parser.add_argument('-d', '--database', dest='db', help='database location dir')
    args = parser.parse_args()
    origin_dir = args.origin_dir
    dest_dir = args.dest_dir

    if os.path.isdir(origin_dir):
        print(f'Using origin video directory "{origin_dir}"')
    else:
        print(f'Given origin video directory path "{origin_dir}" is not a directory')
        exit(1)

    if os.path.isdir(dest_dir):
        print(f'Using destination video directory "{dest_dir}"')
    else:
        print(f'Given destination video directory path "{dest_dir}" is not a directory')
        exit(1)

    db_dir = args.db
    if db_dir:
        print(f'Database Path Given "{db_dir}"')
    else:
        db_dir = dest_dir
        print(f'Using Database Directory "{db_dir}"')

    main(origin_dir, dest_dir, db_dir)
