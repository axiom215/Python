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