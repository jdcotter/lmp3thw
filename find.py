#! /usr/bin/env python3

# cat command in python
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(
                    prog='find',
                    description='Search for files of a directory',
                    epilog='bare bones version of UNIX command "find"')
parser.add_argument('start_dir', metavar='START_DIR', type=str)
parser.add_argument('-n', '--name', help='pattern of files to match on')
args = parser.parse_args()

# get find args -- starting directory
dir = args.start_dir
print('Directory to start search from: ', dir)
p = Path(dir)

# identify pattern to search for, if any
fpat = "**/"
if args.name is None:
    fpat += "*"
else:
    fpat += args.name
print('File pattern is: ', fpat)

# open directory, get list of files
files = list(p.glob(fpat))
      
for file in files:
    print(file)

