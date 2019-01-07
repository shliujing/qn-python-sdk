import hashlib
import sys

data = sys.argv[1]
hash_md5 = hashlib.md5(data)

print(hash_md5.hexdigest())
