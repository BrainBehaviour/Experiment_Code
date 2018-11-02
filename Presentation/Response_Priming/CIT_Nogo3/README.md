# CIT Nogo3

A modified response-priming paradigm employed in stroke patients presenting with chronic low function upper-limb hemiparesis, whilst EEG was recorded.

_Experiment setup:_

	Four white precue stimuli (S1) presented within an empty line-drawn white circle on a black background: 

		valid left (<<), valid right (>>), neutral (< >) or no response (><)

	Are followed by one of three possible response stimuli (S2), represented by a white semicircle appearing within the line-drawn circle

		left button (left white semicircle), right button (right white semicircle) or no button (bottom white semicircle)

	Left, right and no response precues always predict the response correctly. (100% Valid)

	Neutral precues predict a response, but not the response hand. 

Full-preparation trials (40%; valid left [20%], valid right [20%]) and neutral trials (40%) are equally likely, with no response trials half as likely (20%). 

All trial types are randomised within each block.

_Trial Setup:_

	Trials start with an empty line-drawn circle (fixation circle) for 500ms. 

	S1 is presented within the circle for 150 ms, followed by an inter-stimuli interval (empty line-drawn circle) of 1150 ms

	S2 is presented within the circle 1300 ms after S1, until either a response is registered or the end of trial (max.response time = 1.7 s)

	Feedback is displayed for 500 ms and comprises the following: 
	
		correct responses (‘Correct!’); incorrect responses (‘Wrong!’; ‘Don’t Respond!’; ‘Too Late!’), and responses within 200 ms of S2 (‘Too Early!’). 

	After feedback the screen turns grey for 900 ms to signal the end of trial and allow participants to blink/move their eyes.

_Parallel Port Codes_
	
	Precue Right:       T 11
	
	Precue Left:        T 12
	
	Precue Neutral:     T 13	_(if followed by Cue Right)_
	
	Precue Neutral:     T 14	_(if followed by Cue Left)_
	
	Precue No Response: T 15
	
	Cue Right:          T 20	_(if preceded by Precue Right)_
	
	Cue Left:           T 21	_(if preceded by Precue Left)_
	
	Cue Right:          T 22	_(if preceded by Precue Neutral)_
	
	Cue Left:           T 23	_(if preceded by Precue Neutral)_
	
	Cue No Response:    T 24
	
	Feedback Correct:   T 30	_(if Precue Right-Cue Right)_
	
	Feedback Correct:   T 31	_(if Precue Left-Cue Left)_
	
	Feedback Correct:   T 32	_(if Precue Neutral-Cue Right)_
	
	Feedback Correct:   T 33	_(if Precue Neutral-Cue Left)_
	
	Feedback Correct:   T 34	_(if Precue No Response-Cue No Response)_
	
	Feedback Wrong:     T 70	
	
	Feedback Too Early: T 71	
	
	Feedback Too Late:  T 72	
	
	Feedback Don't Respond:  T 73	
	
	Experiment Paused:  T 50	
	
	End of Block:       T 60	

Used in:

Dean PJA, Seiss E, Sterr A (2012) Motor Planning in Chronic Upper-Limb Hemiparesis: Evidence from Movement-Related Potentials. PLoS ONE 7(10): e44558. https://doi.org/10.1371/journal.pone.0044558
