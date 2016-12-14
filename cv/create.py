#!/usr/bin/env python
""" This script builds the Appendix.
"""

# standard library
import os

for type_ in ['pdflatex']:
    os.system(type_ + ' main')
