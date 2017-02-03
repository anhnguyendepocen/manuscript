#!/usr/bin/env python
""" This script builds the all the submission material.
"""

# standard library
import shutil
import os

DIRECTORIES = ['paper', 'appendix', 'letter']

for _ in range(2):
    for dir_ in DIRECTORIES:
        print(dir_)
        os.chdir(dir_)
        os.system('python create.py')
        shutil.move('main.pdf', '../' + dir_ + '.pdf')
        os.chdir('../')

# I need to manually add the cv.
os.chdir('_submodules/curriculum_vitae/sources')
os.system('pdflatex eisenhauer_cv.tex')
shutil.move('eisenhauer_cv.pdf', '../../../cv.pdf')
os.chdir('../../../')

# Concatenate all for the submission.
cmd = 'pdftk paper.pdf appendix.pdf cat output eisenhauer-manuscript.pdf'
os.system(cmd)

cmd = 'pdftk letter.pdf cv.pdf cat output eisenhauer-letter.pdf'
os.system(cmd)

for dir_ in DIRECTORIES + ['cv']:
    os.unlink(dir_ + '.pdf')

# Cleanup subdirectories
for dir_ in DIRECTORIES:
    os.chdir(dir_)
    os.system('git clean -d -f')
    os.chdir('../')
