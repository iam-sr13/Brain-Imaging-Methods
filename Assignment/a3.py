"""
Brain Imaging Methods | Assignment - III | Behavioral Study | Psychopy Stroop Test

@Author: Shriraj  Sawant
@Roll_No: 19350006
@PhD_Scholar 
@BRaINLab_IITGN

"""
###############################################################################
#Import core psychopy libraries for running experiment

from psychopy import monitors, data, gui, visual, core, logging, event  
from datetime import datetime 
from psychopy.hardware import keyboard 

# Define a monitor
my_monitor = monitors.Monitor(name='my_tv')
my_monitor.setSizePix((1024, 768))
my_monitor.setWidth(30)
my_monitor.setDistance(30)
my_monitor.saveMon()

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

def write_csv(fileName, thisTrial):
    """Function for writing data in csv format"""
    full_path = os.path.abspath(fileName)
    directory = os.path.dirname(full_path)
    create_dir(directory)

    if not os.path.isfile(full_path):
        with codecs.open(full_path, 'ab+', encoding='utf8') as f:
            csv.writer(f, delimiter=';').writerow(thisTrial.keys())
            csv.writer(f, delimiter=';').writerow(thisTrial.values())
    else:
        with codecs.open(full_path, 'ab+', encoding='utf8') as f:
            csv.writer(f, delimiter=';').writerow(thisTrial.values())
            
#######################################################################

#Create class for setting up and executing stroop experiment, using object oriented programming
class Stroop_test:
    def __init__(self, win_color): #class constructor, basically initialise class variables
        self.stimuli_positions = [[-.2, 0], [.2, 0], [0, 0]]
        self.win_color = win_color

    def create_window(self, color=(1, 1, 1)): #create window for displaying experiment
        
        color = self.win_color
        win = visual.Window(monitor="testMonitor",
                            color=color, fullscr=True)
        return win

    def settings(self): #Set default experiment variables
        experiment_info = {'Subid': '', 'Age': '', 'Experiment Version': 0.1,
                           'Sex': ['Male', 'Female', 'Other'],
                           'Language': ['English'], u'date':
                               data.getDateStr(format="%Y-%m-%d_%H:%M")}

        info_dialog = gui.DlgFromDict(title='Stroop task', dictionary=experiment_info,
                                      fixed=['Experiment Version'])
        experiment_info[u'DataFile'] = u'Data' + os.path.sep + u'stroop.csv'

        if info_dialog.OK:
            return experiment_info
        else:
            core.quit()
            return 'Cancelled'
        



