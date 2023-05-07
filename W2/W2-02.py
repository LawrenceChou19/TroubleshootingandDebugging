# Real
# user
# sys

# #combined with meeting_reminder
# time ./send_reminders.py "2023-05-06|Example|test1"

# time ./send_reminders.py "2023-05-06|Example|test1,test2,test3,test4,test5,test6,test7,test8,test9"
# #install first
# sudo apt install python3-pprofile 
# pprofile3 -f callgrind -o profile.out ./send_reminders.py "2023-05-06|Example|test1,test2,test3,test4,test5,test6,test7,test8,test9"

# kcachegrind profile.out



# Practice for Performance
#!/usr/bin/env python3


import argparse
import logging
import os
import sys

import PIL
import PIL.Image

from tqdm import tqdm

def process_options():
    kwargs = {
        'format': '[%(levelname)s] %(message)s'
    }
    parser = argparse.ArgumentParser(
    description='Thumbnail generator',
    fromfile_prefix_chars='@'
    )
    parser.add_argument('--debug',action='store_true')
    parser.add_argument('-v','--verbose',action='store_true')
    parser.add_argument('-q','--quiet',action='store_true')

    options = parser.parse_args()

    if options.debug:
        kwargs['level'] = logging.DEBUG
    elif options.verbose:
        kwargs['level'] = logging.INFO
    elif options.quiet:
        kwargs['level'] = logging.ERROR
    else:
        kwargs['level'] = logging.WARN
    logging.basicConfig(**kwargs)
    return options
    
def process_file(root,username):
    filename= f'{root}/{basename}'
    image = PIL.Image.open(filename)

    size = (128,128)
    image.thumbnail(size)

    new_name = f'thumbnails/{basename}'
    image.save(new_name,"JPEG")
    return new_name

def progress_bar(files):
    return tqdm(files,desc='Processing', total=len(files),dynamic_ncols=True)

def main():
    process_options()

    #Create the thumbnails directory
    if not os.path.exists('thumbnails'):
        os.mkdir('thumbnails')
   
    for root,_,files in os.walk('images'):
        for basename in progress_bar(files):
            if not basename.endswith('.jpg'):
                continue
            process_file(root,basename)
            
    return 0
    
if __name__ == "__main__":
    sys.exit(main())