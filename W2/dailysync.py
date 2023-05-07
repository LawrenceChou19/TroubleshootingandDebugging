#!/usr/bin/env python
from multiprocessing import Pool
import multiprocessing
import subprocess
import os
original_path = os.path.expanduser('~')
src = original_path + "/data/prod/"
dest = original_path + "/data/prod_backup/"

if __name__ == "__main__":
        pool = Pool(multiprocessing.cpu_count())
        pool.apply(subprocess.call,args=(["rsync", "-arq", src, dest],))
