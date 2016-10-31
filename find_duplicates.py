"""
find_duplicates.py takes a directory path as an argument and recursively traverses the target directory
to locate all of the files (excluding folders). The files are then MD5 hashed and added to a dictionary<filepath:md5_checksum>.
Once all files are hashed, any dictionary entries with matching MD5 checksums are added to another dictionary and then
the contents of that dictionary are echoed to the screen, indicating the filepath/files that are duplicates.

usage example:
>python find_duplicates.py 'C:\\Users\\josh.terry\\Desktop\\test'

Constraints: This utility should not be used on directories with files that are several gigabytes in size.
Attempting to pull large files into memory to MD5 hash them is beyond what this script is designed to do.

TO DO:
-Clean up output
-Figure out some way to hash chunks of a file and combine those chunks.
(This will allow the script to be pointed at directories with large files.)
"""

import hashlib, sys, os

hashed = {}
duplicates = {}

def md5_hash(path):
    return hashlib.md5(open(path, 'rb').read()).hexdigest()

for (dir, _, files) in os.walk(sys.argv[1]):
    for file in files:
        path = os.path.join(dir, file)
        if os.path.exists(path):
            hashed[path] = md5_hash(path)

for k,v in hashed.items(): 
    if v in duplicates.keys():
        duplicates[v].append(k)
    else:
        duplicates[v] = [k]
                   
for k,v in duplicates.items():
    if len(v) > 1:
        print("The following list of files matched this MD5 checksum: " + k)
        print(v)
        print("Found " + str(len(v)) + " duplicates.")
        print("\n")