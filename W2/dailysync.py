#install sudo apt install python3-pip and sudo apt-get install python3-psutil
#
#!/usr/bin/env python
from multiprocessing import Pool
import multiprocessing
import subprocess
import os
#identify path from the os
original_path = os.path.expanduser('~')
#adding the path with src and dest path
src = original_path + "/data/prod/"
dest = original_path + "/data/prod_backup/"

if __name__ == "__main__":
        pool = Pool(multiprocessing.cpu_count())
        pool.apply(subprocess.call,args=(["rsync", "-arq", src, dest],))
