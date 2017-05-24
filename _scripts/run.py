#!/usr/bin/env python
""" This script builds the all the submission material.
"""

# standard library
import shutil
import os

DIRECTORIES = ['paper', 'appendix', 'notes', 'responses', 'letter']

for _ in range(2):
    for dir_ in DIRECTORIES:
        print(dir_)
        os.chdir(dir_)
        os.system('python create.py')
        shutil.move('main.pdf', '../' + dir_ + '.pdf')
        os.chdir('../')

# Concatenate all for the submission.
cmd = 'pdftk letter.pdf responses.pdf paper.pdf appendix.pdf notes.pdf cat output eisenhauer-full.pdf'
os.system(cmd)

# Cleanup subdirectories
for dir_ in DIRECTORIES:
    os.chdir(dir_)
    os.system('git clean -d -f')
    os.chdir('../')
