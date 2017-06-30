#!/usr/bin/env python
""" This script builds the all the submission material.
"""

# standard library
import shutil
import os

DIRECTORIES = ['paper', 'appendix', 'responses', 'letter']

for _ in range(2):
    for dir_ in DIRECTORIES:
        print(dir_)
        os.chdir(dir_)
        os.system('python create.py')
        shutil.move('main.pdf', '../' + dir_ + '.pdf')
        os.chdir('../')

# Concatenate all for the review.
cmd = 'pdftk letter.pdf responses.pdf paper.pdf appendix.pdf cat output eisenhauer-full.pdf'
os.system(cmd)

# Concatenate all for the submission and some additional renaming.
cmd = 'pdftk paper.pdf appendix.pdf cat output eisenhauer-manuscript.pdf'
os.system(cmd)

for label in ['letter', 'responses']:
    shutil.copy(label + '.pdf', 'eisenhauer-' + label + '.pdf')

# Cleanup subdirectories
for dir_ in DIRECTORIES:
    os.chdir(dir_)
    os.system('git clean -d -f')
    os.chdir('../')
