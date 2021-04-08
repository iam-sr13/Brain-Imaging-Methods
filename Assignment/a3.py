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
        
    def create_trials(self, trial_file, randomization='random'):
        #Generate random stroop test trials from samples stored in file
        data_types = ['Response', 'Accuracy', 'RT', 'Sub_id', 'Sex']
        with open(trial_file, 'r') as stimfile:
            _stims = csv.DictReader(stimfile)
            trials = data.TrialHandler(list(_stims), 1,
                                       method="random")

        [trials.data.addDataType(data_type) for data_type in data_types]

        return trials

    def running_experiment(self, trials, testtype):
        #execute experiment 
        #two modes: Practice Vs Test
        #Practice mode records no behavioral data whereas Test mode considers Response Time and other data
        
        _trials = trials
        testtype = testtype
        timer = core.Clock()
        
        #Create text stimuli
        stimuli = [visual.TextStim(win=window, ori=0, name='', text=None, font=u'Arial', pos=[0.0, 0.0], color='Black', colorSpace=u'rgb') for _ in range(4)]

        for trial in _trials:
            # Stimuli for Fixation cross
            fixation = stimuli[3]
            fixation.pos = self.stimuli_positions[2]
            fixation.setColor('Black')
            fixation.setText('+')
            
            #draw fixation cross
            fixation.draw()
            window.flip()
            core.wait(.6)
            timer.reset()

            # Target word
            target = stimuli[0]
            target.pos = self.stimuli_positions[2]
            target.setColor(trial['colour'])
            target.setText(trial['stimulus'])            
            target.draw()
            
            # Choice 1
            choice1 = stimuli[1]
            choice1.pos = self.stimuli_positions[0]
            choice1.setColor('Black')
            choice1.setText(trial['alt1']) 
            choice1.draw()
            
            # Choice 2
            choice2 = stimuli[2]
            choice2.pos = self.stimuli_positions[1]
            choice2.setColor('Black')
            choice2.setText(trial['alt2']) 
            choice2.draw()
            
            #Wait for user response
            window.flip()
            keys = event.waitKeys(keyList=['x', 'm'])
            resp_time = timer.getTime()
            if testtype == 'practice':
                if keys[0] != trial['correctresponse']:
                    instruction_stimuli['incorrect'].draw()
                else:
                    instruction_stimuli['right'].draw()

                window.flip()
                core.wait(2)

            if testtype == 'test':
                if keys[0] == trial['correctresponse']:
                    trial['Accuracy'] = 1
                else:
                    trial['Accuracy'] = 0

                trial['RT'] = resp_time
                trial['Response'] = keys[0]
                trial['Sub_id'] = settings['Subid']
                trial['Sex'] = settings['Sex']
                write_csv(settings[u'DataFile'], trial)

            event.clearEvents()
        
############################################################################
            
def create_instructions_dict(instr):
    start_n_end = [w for w in instr.split() if w.endswith('START') or w.endswith('END')]
    keys = {}

    for word in start_n_end:
        key = re.split("[END, START]", word)[0]

        if key not in keys.keys():
            keys[key] = []

        if word.startswith(key):
            keys[key].append(word)
    return keys


def create_instructions(input, START, END):
    instruction_text = parse_instructions(input, START, END)
    print(instruction_text)
    text_stimuli = visual.TextStim(window, text=instruction_text, wrapWidth=1.2,
                                   alignHoriz='center', color="Black",
                                   alignVert='center', height=0.06)

    return text_stimuli


def display_instructions(start_instruction=''):
    # Display instructions

    if start_instruction == 'Practice':
        instruction_stimuli['instructions'].pos = (0.0, 0.5)
        instruction_stimuli['instructions'].draw()

        positions = [[-.2, 0], [.2, 0], [0, 0]]
        examples = [visual.TextStim(win=window, ori=0, name='', text=None, font=u'Arial', pos=[0.0, 0.0], color='Black', colorSpace=u'rgb') for pos in positions]
        example_words = ['green', 'blue', 'green']
        
        for i, pos in enumerate(positions):
            examples[i].pos = pos

            if i == 0:
                examples[0].setText(example_words[i])

            elif i == 1:
                examples[1].setText(example_words[i])

            elif i == 2:
                examples[2].setColor('Green')
                examples[2].setText(example_words[i])

        [example.draw() for example in examples]

        instruction_stimuli['practice'].pos = (0.0, -0.5)
        instruction_stimuli['practice'].draw()

    elif start_instruction == 'Test':
        instruction_stimuli['test'].draw()

    elif start_instruction == 'End':
        instruction_stimuli['done'].draw()

    window.flip()
    event.waitKeys(keyList=['space'])
    event.clearEvents()
    
    
if __name__ == "__main__":
    #Initialise Experiment
    experiment = Stroop_test(win_color="White")
    settings = experiment.settings() #extract settings
    language = settings['Language']
    
    #read and display instructions
    instructions = read_instructions_file("instructions.dat", language, language + "End") 
    instructions_dict = create_instructions_dict(instructions)
    instruction_stimuli = {}
    window = experiment.create_window(color=(0, 0, 0))
    for instruction, (START, END) in instructions_dict.items():
        instruction_stimuli[instruction] = create_instructions(instructions, START, END)
        
    #Make mouse invisible to prevent distractions
    event.Mouse(visible=False)
    
    # Practice Trials
    display_instructions(start_instruction='Practice')
    practice = experiment.create_trials('stroop_samples.csv')
    experiment.running_experiment(practice, testtype='practice')
    
    # Test trials
    display_instructions(start_instruction='Test')
    trials = experiment.create_trials('stroop_test.csv')
    experiment.running_experiment(trials, testtype='test')

    # End experiment but first we display some instructions
    display_instructions(start_instruction='End')
    window.close()    



