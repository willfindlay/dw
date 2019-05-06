#! /usr/bin/env python3

import os
import sys
import argparse
import re

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Walk a directory and output all leaf nodes (files).")
    parser.add_argument('-H', '--hidden', dest='show_hidden', action='store_const', default=0, const=1,
                        help='Walk hidden files and directories. (Default setting: Off)')
    parser.add_argument('-d', '--dir', dest='directory', type=str, default=os.getcwd(),
                        help='Choose a directory to walk. (Default setting: Current working directory)')
    parser.add_argument('-o', '--out', metavar="FILE", dest='out', type=str, default=None,
                        help='Output results to <FILE> instead of stdout. (Default setting: Off)')
    # TODO: maybe add this to a future version
    #parser.add_argument('-l', '--level', dest='level', type=int, default=None,
    #                    help='Choose a maximum depth from 0 (ls current directory) to whatever value you like. (Default setting: No maximum)')

    args = parser.parse_args()

    # maybe redirect output
    if args.out is not None:
        sys.stdout = open(args.out, "w")

    path = args.directory
    for dirpath, dirnames, files in os.walk(path):
        # don't walk hidden directories unless specified
        if not args.show_hidden:
            if re.search(r"(\/\.|^\.)",dirpath):
                continue
        # print all files
        for f in files:
            # don't show hidden files unless specified
            if not args.show_hidden:
                if re.search(r"^\.",f):
                    continue
            print(os.path.join(dirpath, f))
