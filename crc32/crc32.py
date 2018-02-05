import zlib
import sys

if len(sys.argv) != 2:
    exit(1)

f = open(sys.argv[1], "rb")
print("0x%08x" % zlib.crc32(f.read()))
