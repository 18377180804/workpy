import sys
import hashlib

# gpus = sys.argv[1]
# gpus = [int(gpus.split(','))]

gpus='你好'


hsobj = hashlib.sha256(gpus.encode("utf-8"))
print(hsobj.hexdigest())
