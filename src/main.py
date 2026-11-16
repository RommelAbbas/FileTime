import os
from os import pread

for root, dirs, files in os.walk("/home/rommel/filetime-test"):
    print(root)