# Eye Topographies  

Simple task where participants are asked to keep their head still and follow a moving circle with their eyes, then blink the circle fills in white. 

This task is run at the beginning of an EEG recording to get a measure of individual eye movement and blink artifacts. 

Ideally, an EEG task would be designed to prevent any eye movements or blinks during a task, or to make them infrequent and random in timing. Furthermore, if eye movements or blinks are seen in the data then either ICA correction or bad segment removal should be performed. 

However, in some cases, such as in clinical populations, it is difficult to meet these criteria and typical correction isnt working, or bad segment removal would drastically reduce trial numbers. 

This task can be used to form a representation of eye movement and blink topographies in software such as BESA. The markers in the EEG file tell you which sort of eye artifact exists, and you can mark this in BESA to form the artifact topography. 

This can be then used to correct your main task data. 

_Task_

There are 5 repeitions of each of the conditions (see below), and these are randomly ordered. 

_Parallel Port Codes_

    Circle at Centre:       T 5

    Left Eye Move:          T 6

    Right Eye Move:         T 7

    Up Eye Move:            T 8

    Down Eye Move:          T 9

    Blink:                  T 10


