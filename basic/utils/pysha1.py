import hashlib
import sys

a = sys.argv[1]
sha1 = hashlib.sha1(a)

print(sha1.hexdigest())
