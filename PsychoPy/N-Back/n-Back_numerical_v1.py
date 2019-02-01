#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.0b12),
    on January 07, 2019, at 13:40
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.0.0b12'
expName = 'n-Back_numerical_v1'  # from the Builder filename that created this script
expInfo = {'session': '001', 'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data' + os.sep + '%s_%s' % (expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Nicon\\Documents\\NICOLA_EXPERIMENTS\\PsychoPy-3.0.0b12\\N-Back\\n-Back_numerical_v1.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-0.15,-0.15,-0.15], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "INST"
INSTClock = core.Clock()
poly = visual.Rect(
    win=win, name='poly',
    width=(2,2)[0], height=(2,2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
text_5 = visual.TextStim(win=win, name='text_5',
    text="This is an n-back task. The n-back task presents stimuli sequentially and require you to decide if the current stimulus is the same as one presented n-numbers previous (or back).  \n\nThere are two parts, a 0-back task, and a 2-back task. \n\nFor the 0-back you will indicate if the current number on the screen matches a defined target. \n\nPress SPACE if it's a target match.\n\nFor the 2-back you will indicate if the current number matches the number presented 2 places previous \n(e.g.  4 6 4 8 9 8 3 1 shows that '4' and '8' are matches in this sequence). \n\nPress SPACE if the current NUMBER is the same a 2 places previous.\n\n\nPress SPACE bar when ready to start. ",
    font='Arial',
    pos=(0,0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "routine_0backinstructions"
routine_0backinstructionsClock = core.Clock()
polygon_5 = visual.Rect(
    win=win, name='polygon_5',
    width=(2,2)[0], height=(2,2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
text_2 = visual.TextStim(win=win, name='text_2',
    text='\n*** 0-back task ***\nDoes the current NUMBER \nmatch the target? ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "routine_0_Back_Target"
routine_0_Back_TargetClock = core.Clock()
Back0Target=[]
thisExp.addData('Back0Target', Back0Target)
polygon = visual.Rect(
    win=win, name='polygon',
    width=(2,2)[0], height=(2,2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
text_3 = visual.TextStim(win=win, name='text_3',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.4, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text = visual.TextStim(win=win, name='text',
    text='TARGET',
    font='Arial',
    pos=[0, 0.5], height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "routine_0_Back"
routine_0_BackClock = core.Clock()
letter=[]


polygon_2 = visual.Rect(
    win=win, name='polygon_2',
    width=(2,2)[0], height=(2,2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
letterText = visual.TextStim(win=win, name='letterText',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.4, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "routine_2backinstruct"
routine_2backinstructClock = core.Clock()
polygon_4 = visual.Rect(
    win=win, name='polygon_4',
    width=(2,2)[0], height=(2,2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
back2_instruc = visual.TextStim(win=win, name='back2_instruc',
    text='\n*** 2-back task ***\nDoes the current NUMBER match that \npresented 2 NUMBERS previous? \n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "routine_2_Back_Target"
routine_2_Back_TargetClock = core.Clock()
Back2minus1=[]
Back2minus2=[]
polygon_6 = visual.Rect(
    win=win, name='polygon_6',
    width=(2,2)[0], height=(2,2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
text3 = visual.TextStim(win=win, name='text3',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.4, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "routine_2_Back"
routine_2_BackClock = core.Clock()

polygon_7 = visual.Rect(
    win=win, name='polygon_7',
    width=(2,2)[0], height=(2,2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
text_4 = visual.TextStim(win=win, name='text_4',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.4, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "finish"
finishClock = core.Clock()
polygon_8 = visual.Rect(
    win=win, name='polygon_8',
    width=(2,2)[0], height=(2,2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
text_6 = visual.TextStim(win=win, name='text_6',
    text='This experiment is over',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "INST"-------
t = 0
INSTClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_4 = event.BuilderKeyResponse()
# keep track of which components have finished
INSTComponents = [poly, text_5, key_resp_4]
for thisComponent in INSTComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "INST"-------
while continueRoutine:
    # get current time
    t = INSTClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *poly* updates
    if t >= 0.0 and poly.status == NOT_STARTED:
        # keep track of start time/frame for later
        poly.tStart = t
        poly.frameNStart = frameN  # exact frame index
        poly.setAutoDraw(True)
    
    # *text_5* updates
    if t >= 0.0 and text_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_5.tStart = t
        text_5.frameNStart = frameN  # exact frame index
        text_5.setAutoDraw(True)
    
    # *key_resp_4* updates
    if t >= 0.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_4.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_4.keys = theseKeys[-1]  # just the last key pressed
            key_resp_4.rt = key_resp_4.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in INSTComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "INST"-------
for thisComponent in INSTComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys=None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.nextEntry()
# the Routine "INST" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=3, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "routine_0backinstructions"-------
    t = 0
    routine_0backinstructionsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(7.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    routine_0backinstructionsComponents = [polygon_5, text_2]
    for thisComponent in routine_0backinstructionsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "routine_0backinstructions"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = routine_0backinstructionsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_5* updates
        if t >= 0.0 and polygon_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_5.tStart = t
            polygon_5.frameNStart = frameN  # exact frame index
            polygon_5.setAutoDraw(True)
        frameRemains = 0.0 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
        if polygon_5.status == STARTED and t >= frameRemains:
            polygon_5.setAutoDraw(False)
        
        # *text_2* updates
        if t >= 0.0 and text_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_2.tStart = t
            text_2.frameNStart = frameN  # exact frame index
            text_2.setAutoDraw(True)
        frameRemains = 0.0 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_2.status == STARTED and t >= frameRemains:
            text_2.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in routine_0backinstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "routine_0backinstructions"-------
    for thisComponent in routine_0backinstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # set up handler to look after randomisation of conditions etc
    Back0Loop = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='Back0Loop')
    thisExp.addLoop(Back0Loop)  # add the loop to the experiment
    thisBack0Loop = Back0Loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBack0Loop.rgb)
    if thisBack0Loop != None:
        for paramName in thisBack0Loop:
            exec('{} = thisBack0Loop[paramName]'.format(paramName))
    
    for thisBack0Loop in Back0Loop:
        currentLoop = Back0Loop
        # abbreviate parameter names if possible (e.g. rgb = thisBack0Loop.rgb)
        if thisBack0Loop != None:
            for paramName in thisBack0Loop:
                exec('{} = thisBack0Loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "routine_0_Back_Target"-------
        t = 0
        routine_0_Back_TargetClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.500000)
        # update component parameters for each repeat
        
        letters = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        from random import choice
        Back0Target=choice(letters)
        
        
        text_3.setText(Back0Target)
        # keep track of which components have finished
        routine_0_Back_TargetComponents = [polygon, text_3, text]
        for thisComponent in routine_0_Back_TargetComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "routine_0_Back_Target"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = routine_0_Back_TargetClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *polygon* updates
            if t >= 0.0 and polygon.status == NOT_STARTED:
                # keep track of start time/frame for later
                polygon.tStart = t
                polygon.frameNStart = frameN  # exact frame index
                polygon.setAutoDraw(True)
            frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if polygon.status == STARTED and t >= frameRemains:
                polygon.setAutoDraw(False)
            
            # *text_3* updates
            if t >= 0.0 and text_3.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_3.tStart = t
                text_3.frameNStart = frameN  # exact frame index
                text_3.setAutoDraw(True)
            frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_3.status == STARTED and t >= frameRemains:
                text_3.setAutoDraw(False)
            
            # *text* updates
            if t >= 0.0 and text.status == NOT_STARTED:
                # keep track of start time/frame for later
                text.tStart = t
                text.frameNStart = frameN  # exact frame index
                text.setAutoDraw(True)
            frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text.status == STARTED and t >= frameRemains:
                text.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in routine_0_Back_TargetComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "routine_0_Back_Target"-------
        for thisComponent in routine_0_Back_TargetComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        
        # set up handler to look after randomisation of conditions etc
        Back0TrialsLoop = data.TrialHandler(nReps=20, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('stim\\0-back_loop.xlsx'),
            seed=None, name='Back0TrialsLoop')
        thisExp.addLoop(Back0TrialsLoop)  # add the loop to the experiment
        thisBack0TrialsLoop = Back0TrialsLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisBack0TrialsLoop.rgb)
        if thisBack0TrialsLoop != None:
            for paramName in thisBack0TrialsLoop:
                exec('{} = thisBack0TrialsLoop[paramName]'.format(paramName))
        
        for thisBack0TrialsLoop in Back0TrialsLoop:
            currentLoop = Back0TrialsLoop
            # abbreviate parameter names if possible (e.g. rgb = thisBack0TrialsLoop.rgb)
            if thisBack0TrialsLoop != None:
                for paramName in thisBack0TrialsLoop:
                    exec('{} = thisBack0TrialsLoop[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "routine_0_Back"-------
            t = 0
            routine_0_BackClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(1.200000)
            # update component parameters for each repeat
            if trialType=='nonTarget':
                letters = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
                from random import choice
                letter=choice(letters)
            elif trialType=='target':
                letter=Back0Target 
            
            
            letterText.setText(letter)
            key_resp_2 = event.BuilderKeyResponse()
            # keep track of which components have finished
            routine_0_BackComponents = [polygon_2, letterText, key_resp_2]
            for thisComponent in routine_0_BackComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "routine_0_Back"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = routine_0_BackClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                
                # *polygon_2* updates
                if t >= 0.0 and polygon_2.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    polygon_2.tStart = t
                    polygon_2.frameNStart = frameN  # exact frame index
                    polygon_2.setAutoDraw(True)
                frameRemains = 0.0 + 1.2- win.monitorFramePeriod * 0.75  # most of one frame period left
                if polygon_2.status == STARTED and t >= frameRemains:
                    polygon_2.setAutoDraw(False)
                
                # *letterText* updates
                if t >= 0.0 and letterText.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    letterText.tStart = t
                    letterText.frameNStart = frameN  # exact frame index
                    letterText.setAutoDraw(True)
                frameRemains = 0.0 + 0.8- win.monitorFramePeriod * 0.75  # most of one frame period left
                if letterText.status == STARTED and t >= frameRemains:
                    letterText.setAutoDraw(False)
                if letterText.status == STARTED:  # only update if drawing
                    letterText.setPos([0, 0], log=False)
                
                # *key_resp_2* updates
                if t >= 0.0 and key_resp_2.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    key_resp_2.tStart = t
                    key_resp_2.frameNStart = frameN  # exact frame index
                    key_resp_2.status = STARTED
                    # keyboard checking is just starting
                    win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                frameRemains = 0.0 + 1.2- win.monitorFramePeriod * 0.75  # most of one frame period left
                if key_resp_2.status == STARTED and t >= frameRemains:
                    key_resp_2.status = STOPPED
                if key_resp_2.status == STARTED:
                    theseKeys = event.getKeys(keyList=['space'])
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        if key_resp_2.keys == []:  # then this was the first keypress
                            key_resp_2.keys = theseKeys[0]  # just the first key pressed
                            key_resp_2.rt = key_resp_2.clock.getTime()
                            # was this 'correct'?
                            if (key_resp_2.keys == str(corrResponse)) or (key_resp_2.keys == corrResponse):
                                key_resp_2.corr = 1
                            else:
                                key_resp_2.corr = 0
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in routine_0_BackComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "routine_0_Back"-------
            for thisComponent in routine_0_BackComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            # check responses
            if key_resp_2.keys in ['', [], None]:  # No response was made
                key_resp_2.keys=None
                # was no response the correct answer?!
                if str(corrResponse).lower() == 'none':
                   key_resp_2.corr = 1;  # correct non-response
                else:
                   key_resp_2.corr = 0;  # failed to respond (incorrectly)
            # store data for Back0TrialsLoop (TrialHandler)
            Back0TrialsLoop.addData('key_resp_2.keys',key_resp_2.keys)
            Back0TrialsLoop.addData('key_resp_2.corr', key_resp_2.corr)
            if key_resp_2.keys != None:  # we had a response
                Back0TrialsLoop.addData('key_resp_2.rt', key_resp_2.rt)
            thisExp.nextEntry()
            
        # completed 20 repeats of 'Back0TrialsLoop'
        
        # get names of stimulus parameters
        if Back0TrialsLoop.trialList in ([], [None], None):
            params = []
        else:
            params = Back0TrialsLoop.trialList[0].keys()
        # save data for this loop
        Back0TrialsLoop.saveAsExcel(filename + '.xlsx', sheetName='Back0TrialsLoop',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        thisExp.nextEntry()
        
    # completed 1 repeats of 'Back0Loop'
    
    # get names of stimulus parameters
    if Back0Loop.trialList in ([], [None], None):
        params = []
    else:
        params = Back0Loop.trialList[0].keys()
    # save data for this loop
    Back0Loop.saveAsExcel(filename + '.xlsx', sheetName='Back0Loop',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # ------Prepare to start Routine "routine_2backinstruct"-------
    t = 0
    routine_2backinstructClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(7.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    routine_2backinstructComponents = [polygon_4, back2_instruc]
    for thisComponent in routine_2backinstructComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "routine_2backinstruct"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = routine_2backinstructClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_4* updates
        if t >= 0.0 and polygon_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_4.tStart = t
            polygon_4.frameNStart = frameN  # exact frame index
            polygon_4.setAutoDraw(True)
        frameRemains = 0.0 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
        if polygon_4.status == STARTED and t >= frameRemains:
            polygon_4.setAutoDraw(False)
        
        # *back2_instruc* updates
        if t >= 0.0 and back2_instruc.status == NOT_STARTED:
            # keep track of start time/frame for later
            back2_instruc.tStart = t
            back2_instruc.frameNStart = frameN  # exact frame index
            back2_instruc.setAutoDraw(True)
        frameRemains = 0.0 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
        if back2_instruc.status == STARTED and t >= frameRemains:
            back2_instruc.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in routine_2backinstructComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "routine_2backinstruct"-------
    for thisComponent in routine_2backinstructComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # set up handler to look after randomisation of conditions etc
    Back2Loop = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='Back2Loop')
    thisExp.addLoop(Back2Loop)  # add the loop to the experiment
    thisBack2Loop = Back2Loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBack2Loop.rgb)
    if thisBack2Loop != None:
        for paramName in thisBack2Loop:
            exec('{} = thisBack2Loop[paramName]'.format(paramName))
    
    for thisBack2Loop in Back2Loop:
        currentLoop = Back2Loop
        # abbreviate parameter names if possible (e.g. rgb = thisBack2Loop.rgb)
        if thisBack2Loop != None:
            for paramName in thisBack2Loop:
                exec('{} = thisBack2Loop[paramName]'.format(paramName))
        
        # set up handler to look after randomisation of conditions etc
        Back2TargetLoop = data.TrialHandler(nReps=2, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='Back2TargetLoop')
        thisExp.addLoop(Back2TargetLoop)  # add the loop to the experiment
        thisBack2TargetLoop = Back2TargetLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisBack2TargetLoop.rgb)
        if thisBack2TargetLoop != None:
            for paramName in thisBack2TargetLoop:
                exec('{} = thisBack2TargetLoop[paramName]'.format(paramName))
        
        for thisBack2TargetLoop in Back2TargetLoop:
            currentLoop = Back2TargetLoop
            # abbreviate parameter names if possible (e.g. rgb = thisBack2TargetLoop.rgb)
            if thisBack2TargetLoop != None:
                for paramName in thisBack2TargetLoop:
                    exec('{} = thisBack2TargetLoop[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "routine_2_Back_Target"-------
            t = 0
            routine_2_Back_TargetClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(1.200000)
            # update component parameters for each repeat
            letters = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            from random import choice
            letter=choice(letters)
            
            text3.setText(letter)
            # keep track of which components have finished
            routine_2_Back_TargetComponents = [polygon_6, text3]
            for thisComponent in routine_2_Back_TargetComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "routine_2_Back_Target"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = routine_2_Back_TargetClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                
                # *polygon_6* updates
                if t >= 0.0 and polygon_6.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    polygon_6.tStart = t
                    polygon_6.frameNStart = frameN  # exact frame index
                    polygon_6.setAutoDraw(True)
                frameRemains = 0.0 + 1.2- win.monitorFramePeriod * 0.75  # most of one frame period left
                if polygon_6.status == STARTED and t >= frameRemains:
                    polygon_6.setAutoDraw(False)
                
                # *text3* updates
                if t >= 0.0 and text3.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text3.tStart = t
                    text3.frameNStart = frameN  # exact frame index
                    text3.setAutoDraw(True)
                frameRemains = 0.0 + 0.8- win.monitorFramePeriod * 0.75  # most of one frame period left
                if text3.status == STARTED and t >= frameRemains:
                    text3.setAutoDraw(False)
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in routine_2_Back_TargetComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "routine_2_Back_Target"-------
            for thisComponent in routine_2_Back_TargetComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            Back2minus2=Back2minus1
            Back2minus1=letter
            thisExp.nextEntry()
            
        # completed 2 repeats of 'Back2TargetLoop'
        
        # get names of stimulus parameters
        if Back2TargetLoop.trialList in ([], [None], None):
            params = []
        else:
            params = Back2TargetLoop.trialList[0].keys()
        # save data for this loop
        Back2TargetLoop.saveAsExcel(filename + '.xlsx', sheetName='Back2TargetLoop',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # set up handler to look after randomisation of conditions etc
        Back2TrialsLoop = data.TrialHandler(nReps=20, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('stim\\2-back_loop.xlsx'),
            seed=None, name='Back2TrialsLoop')
        thisExp.addLoop(Back2TrialsLoop)  # add the loop to the experiment
        thisBack2TrialsLoop = Back2TrialsLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisBack2TrialsLoop.rgb)
        if thisBack2TrialsLoop != None:
            for paramName in thisBack2TrialsLoop:
                exec('{} = thisBack2TrialsLoop[paramName]'.format(paramName))
        
        for thisBack2TrialsLoop in Back2TrialsLoop:
            currentLoop = Back2TrialsLoop
            # abbreviate parameter names if possible (e.g. rgb = thisBack2TrialsLoop.rgb)
            if thisBack2TrialsLoop != None:
                for paramName in thisBack2TrialsLoop:
                    exec('{} = thisBack2TrialsLoop[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "routine_2_Back"-------
            t = 0
            routine_2_BackClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(1.200000)
            # update component parameters for each repeat
            if trialType=='nonTarget':
                letters = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
                from random import choice
                letter=choice(letters)
                if letter==Back2minus1:
                        from random import choice
                        letter=choice(letters)
            elif trialType=='target':
                letter=Back2minus2
            
            thisExp.addData('trialType',trialType) 
            text_4.setText(letter)
            key_resp_3 = event.BuilderKeyResponse()
            # keep track of which components have finished
            routine_2_BackComponents = [polygon_7, text_4, key_resp_3]
            for thisComponent in routine_2_BackComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "routine_2_Back"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = routine_2_BackClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                
                
                # *polygon_7* updates
                if t >= 0.0 and polygon_7.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    polygon_7.tStart = t
                    polygon_7.frameNStart = frameN  # exact frame index
                    polygon_7.setAutoDraw(True)
                frameRemains = 0.0 + 1.2- win.monitorFramePeriod * 0.75  # most of one frame period left
                if polygon_7.status == STARTED and t >= frameRemains:
                    polygon_7.setAutoDraw(False)
                
                # *text_4* updates
                if t >= 0.0 and text_4.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_4.tStart = t
                    text_4.frameNStart = frameN  # exact frame index
                    text_4.setAutoDraw(True)
                frameRemains = 0.0 + 0.8- win.monitorFramePeriod * 0.75  # most of one frame period left
                if text_4.status == STARTED and t >= frameRemains:
                    text_4.setAutoDraw(False)
                if text_4.status == STARTED:  # only update if drawing
                    text_4.setPos([0, 0], log=False)
                
                # *key_resp_3* updates
                if t >= 0.0 and key_resp_3.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    key_resp_3.tStart = t
                    key_resp_3.frameNStart = frameN  # exact frame index
                    key_resp_3.status = STARTED
                    # keyboard checking is just starting
                    win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                    event.clearEvents(eventType='keyboard')
                frameRemains = 0.0 + 1.2- win.monitorFramePeriod * 0.75  # most of one frame period left
                if key_resp_3.status == STARTED and t >= frameRemains:
                    key_resp_3.status = STOPPED
                if key_resp_3.status == STARTED:
                    theseKeys = event.getKeys(keyList=['space'])
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        if key_resp_3.keys == []:  # then this was the first keypress
                            key_resp_3.keys = theseKeys[0]  # just the first key pressed
                            key_resp_3.rt = key_resp_3.clock.getTime()
                            # was this 'correct'?
                            if (key_resp_3.keys == str(corrResponse)) or (key_resp_3.keys == corrResponse):
                                key_resp_3.corr = 1
                            else:
                                key_resp_3.corr = 0
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in routine_2_BackComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "routine_2_Back"-------
            for thisComponent in routine_2_BackComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            Back2minus2=Back2minus1
            Back2minus1=letter
            
            # check responses
            if key_resp_3.keys in ['', [], None]:  # No response was made
                key_resp_3.keys=None
                # was no response the correct answer?!
                if str(corrResponse).lower() == 'none':
                   key_resp_3.corr = 1;  # correct non-response
                else:
                   key_resp_3.corr = 0;  # failed to respond (incorrectly)
            # store data for Back2TrialsLoop (TrialHandler)
            Back2TrialsLoop.addData('key_resp_3.keys',key_resp_3.keys)
            Back2TrialsLoop.addData('key_resp_3.corr', key_resp_3.corr)
            if key_resp_3.keys != None:  # we had a response
                Back2TrialsLoop.addData('key_resp_3.rt', key_resp_3.rt)
            thisExp.nextEntry()
            
        # completed 20 repeats of 'Back2TrialsLoop'
        
        # get names of stimulus parameters
        if Back2TrialsLoop.trialList in ([], [None], None):
            params = []
        else:
            params = Back2TrialsLoop.trialList[0].keys()
        # save data for this loop
        Back2TrialsLoop.saveAsExcel(filename + '.xlsx', sheetName='Back2TrialsLoop',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        thisExp.nextEntry()
        
    # completed 1 repeats of 'Back2Loop'
    
    # get names of stimulus parameters
    if Back2Loop.trialList in ([], [None], None):
        params = []
    else:
        params = Back2Loop.trialList[0].keys()
    # save data for this loop
    Back2Loop.saveAsExcel(filename + '.xlsx', sheetName='Back2Loop',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    thisExp.nextEntry()
    
# completed 3 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "finish"-------
t = 0
finishClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
finishComponents = [polygon_8, text_6]
for thisComponent in finishComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "finish"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = finishClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon_8* updates
    if t >= 0.0 and polygon_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon_8.tStart = t
        polygon_8.frameNStart = frameN  # exact frame index
        polygon_8.setAutoDraw(True)
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if polygon_8.status == STARTED and t >= frameRemains:
        polygon_8.setAutoDraw(False)
    
    # *text_6* updates
    if t >= 0.0 and text_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_6.tStart = t
        text_6.frameNStart = frameN  # exact frame index
        text_6.setAutoDraw(True)
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_6.status == STARTED and t >= frameRemains:
        text_6.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in finishComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "finish"-------
for thisComponent in finishComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)




# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
