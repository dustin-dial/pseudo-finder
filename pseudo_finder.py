#!/usr/bin/env python3
"""
pseudo_finder.py: A script to find pseudogene candidates in annotated genbank files.
Tested mostly on .gbk files annotated by Prokka with the --compliant flag.

Installation requirements:
    python3
    3rd party libraries: biopython
    libraries from the Python standard library: see annotate.py and visualize.py

 """
__author__ = "Mitch Syberg-Olsen & Filip Husnik"
__version__ = "0.09"
__maintainer__ = "Filip Husnik"
__email__ = "filip.husnik@gmail.com"

from sys import argv, stderr
import annotate, visualize, genome_map

errormessage=("Options: pseudo_finder.py [ annotate | visualize | map | help ]\n")

try:
    if argv[1] == "annotate":
        annotate.main()
    elif argv[1] == "visualize":
        visualize.main()
    elif argv[1] == "map":
        genome_map.main()
    elif argv[1] == "help":
        stderr.write("\tpseudofinder.py annotate: Flags candidate pseudogenes.\n"
                     "\tpseudofinder.py visualize: Generates a 3D plot to visualize different combinations of settings.\n"
                     "\tpseudofinder.py map: Generates a chromosome map to show where pseudogenes have been called.\n")
        exit() #TODO: write a more informative help message
    else:
        stderr.write(errormessage); exit()
except IndexError:
    stderr.write(errormessage); exit()