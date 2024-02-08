#!/usr/bin/python3
import tarfile
import os

# Extract the tar file

def compress(filename,output_filename):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(filename, arcname=os.path.basename(filename))
    print("Compressed")

filename = "test"
output_filename = "test.tar.gz"
compress(filename,output_filename)

