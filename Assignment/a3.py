#Import core psychopy libraries for running experiment

from psychopy import data, gui, visual, core, logging, event  
from datetime import datetime 
from psychopy.hardware import keyboard 

###############################################################################
#Import file handling libraries
import codecs
import csv
import os
import re

#Basic Functions for reading/writing files and folders
def parse_instructions(input, START, END):
    """Function for getting instructions into correct format"""
        m = re.compile(r'%s(.*)%s' % (START, END), re.DOTALL | re.MULTILINE)
        text = m.search(input).group(1)

        return text

def read_instructions_file(instructionsfile, START, END):
    """Function for reading instructions from the file"""
    with codecs.open(instructionsfile, 'r', encoding='utf-8') as instructions:
        input_data = instructions.read()
        text = parse_instructions(input_data, START, END)

    return text

def create_dir(directory):
    """Function for creating folders"""
    if not os.path.exists(directory):
        os.makedirs(directory)
