"""
  Read arguments from command line:
  1. folder name containing images
  2. output file name (includes folder)

  10_argument_parsing -i c:/images -i c:/images/file.pdf
"""

def parse_config():
    import argparse
    import os

    parser = argparse.ArgumentParser(description="Consolidates Image files and creates a PDF")
    parser.add_argument("-i", "--indir",required=True, help="Read images from directory")
    parser.add_argument("-o", "--outfile", required=True, help="Full path of a new pdf to be created")

    return parser.parse_args()

config=parse_config()
srcFolder=config.indir
destFile=config.outfile

print("Input Folder={0}, Output File={1}".format(srcFolder,destFile))