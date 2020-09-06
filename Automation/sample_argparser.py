https://realpython.com/command-line-interfaces-python-argparse/

import sys
import os
import argparse


my_parser = argparse.ArgumentParser()

# positional arguments
my_parser.add_argument('Path',metavar='path',type=str,help='the path to list')

# optional arguments
my_parser.add_argument('--input', action='store', type=int, required=True)
my_parser.add_argument('--id', action='store', type=int)

args = my_parser.parse_args()

print(args.input)
print(args.id)

## Example

python sample_argparser.py /mnt/some --input test1 --id 456
