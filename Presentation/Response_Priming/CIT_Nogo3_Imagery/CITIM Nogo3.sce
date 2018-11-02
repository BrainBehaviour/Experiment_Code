scenario = "CITIM Nogo3_21/06/05";
default_font_size = 25;
pcl_file = "CITIMNogo3_Main.pcl"; 
default_font = "Arial";
default_all_responses = false;
default_background_color = 0,0,0; 
active_buttons = 5;
button_codes = 1,2,3,4,5;
response_matching = simple_matching;
write_codes = true;
pulse_width = 20;
begin;                
picture {} default;  

#Introduction Screen
text{caption = "In each trial you will first see a circle\nthen a pair of arrows will quickly flash inside this circle\nThese arrows tell you how to prepare for the forthcoming response\n\n>> Right hand\n<< Left hand\n<> Right or Left hand\n>< NO Response required\n\nAfter a short delay, half of the circle will become white\nThis tell you which response to imagine\n\nRight Button = Right half of circle lit\nLeft Button = Left half of circle lit\nNO Response = Bottom half of the circle will be lit\n\nPress a button to start training trials";} IntroScreen;

#Training Screen
text{caption = "In this training block you will practice imagining\n\nLeft <<\n\nand\n\nRight >>\n\ntrials only\n\nThe arrows mean get ready to imagine responding\n\nwith the appropriate hand\n\nPress a button to continue";}TrainScreen1; 
text{caption = "In this training block you will practice imagining\n\nNeutral <>\n\ntrials only\n\nThe arrows mean get ready to imagine responding with either hand\n\nPress a button to continue";}TrainScreen2;
text{caption = "In this training block you will practice imagining\n\nNo-response ><\n\ntrials only\n\nThe arrows mean you do not need to prepare to respond\n\nPress a button to continue";}TrainScreen3;

# Open circle
bitmap {filename = "IMOpen Circle.bmp";} IMOpen_Circle;
  
#Precues
bitmap {filename = "IMPrimeRight.bmp";} IMPrime_Right;        # T 11

bitmap {filename = "IMPrimeLeft.bmp";} IMPrime_Left;          # T 12
                                                                                                                                    
bitmap {filename = "IMPrimeNeutral.bmp";} IMPrime_Neutral;    # Right T 13; Left T 14

bitmap {filename = "IMPrimeNo.bmp";} IMPrime_Nogo;            # T 15

   
#Cues  

bitmap {filename = "IMRight Response.bmp";} IMRespond_Right;   # Right T 21, Neutral T 23

bitmap {filename = "IMLeft Response.bmp";} IMRespond_Left;     # Left T 22, Neutral T 24

bitmap {filename = "IMNo Response.bmp";} IMNo_Response;        # T 25


#Response Feedback
text{caption = "Correct";           #   IMRight Valid      T 31
     font_size = 40;                #   IMLeft Valid       T 32
     font_color = 0,255,0;          #   IMNeutral Right    T 33
     }Correct;                      #   IMNeutral Left     T 34
                                    #   IMNogo Valid       T 35
    
                                    

text{caption = "Wrong!";
     font_size = 40;
     font_color = 255,0,0;
   }Wrong;                                           # T 70
text{caption = "Too Early!";
     font_size = 40;
     font_color = 0,0,255;
   }Too_Fast;                                        # T 71
text{caption = "Too Late!";
     font_size = 40;
     font_color = 255,0,0;
   }Wrong_YES;                                       # T 72
text{caption = "Don't Respond!";
     font_size = 40;
     font_color = 255,0,0;
   }Wrong_NO;                                        # T 73

#General Text for Running Experiment
text{caption = "Please keep your eyes fixed\non the centre of the screen\n\n\nPress a button to start training";}Pretrain;
text{caption = "Please keep your eyes fixed\non the centre of the screen";}Pretrial;

text{caption = "!! Please take a break !!\nExperiment has been paused by the experimenter";}Pause;    # T 50
text{caption = "When you are ready to continue press a button";}Continue;     

text{caption = "End of Block:";}Block;               # T 60
text{caption = "<num>";}BlockNumber;                 # The <num> is overwritten by PCL
text{caption = "Percent correct:";}PercentText;
text{caption = "<num>";}PercentCorrect;              # The <num> is overwritten by PCL

# Resume trial
trial{                 
     trial_duration = forever;
     trial_type = first_response;
     all_responses = true;
     
     picture {
            text Continue;
            x = 0; y = 0;
      };
     code = "Cont";   
     
}ResumeTrial; 

# Pause trial
trial{                 
     trial_duration = forever;
     trial_type = first_response;
     all_responses = true;
     
     picture {
            text Pause;
            x = 0; y = 0;
     };
     deltat = 25;
     code = "Pause";   
     port_code = 50;
     
}PauseTrial;

# End of block trial
trial{                 
     trial_duration = forever;
     trial_type = first_response;
     all_responses = true;
     
     picture {
            text Block;  
            x = 0; y = 100; 
            text BlockNumber;
            x = 0; y = 50;   
            text PercentText;
            x = 0; y = 0;
            text PercentCorrect;
            x = 0; y = -50;
     };
     deltat = 25;
     code = "EndBl"; 
     port_code = 60;  
     
}EndTrial; 


# Feedback 

TEMPLATE "Feedback.tem" {
   Feedback    FeedbackCode      FeedbackPortCode     FeedbackName;
   Correct     " T 31"           31                   IMCorrectR;
   Correct     " T 32"           32                   IMCorrectL;
   Correct     " T 33"           33                   IMCorrectNR;
   Correct     " T 34"           34                   IMCorrectNL;
   Correct     " T 35"           35                   IMCorrectNo;                    
   Wrong       " T 70"           70                   FeedbackWrong;
   Too_Fast    " T 71"           71                   toofast;
   Wrong_YES   " T 72"           72                   Responserequired; 
   Wrong_NO    " T 73"           73                   NoResponseRequired;
};    
     
#Introduction Code  

TEMPLATE "IntroScreen.tem" {   
   stext          scode             IntroName;
   IntroScreen    "Intro Screen"    Intro1;
   Pretrain       "Pretrain"        Intro2;
   TrainScreen1   "Train Screen 1"  Intro3;
   TrainScreen2   "Train Screen 2"  Intro4;
   TrainScreen3   "Train Screen 3"  Intro5;
   Pretrial       "Pretrial"        Intro6; 
};


#  The 5 Responses

TEMPLATE "Response.tem" {
   trialduration   WrongFeedbackTrialName  NoFeedbackTrialName  CorrectFeedbackTrialName   CueName          ButtonNumber   CueCode     ResponseTrialName;
   1970            NoResponseRequired      IMCorrectR           NoResponseRequired         IMRespond_Right  2              "IMR-R"     IMResponseR;
   1970            NoResponseRequired      IMCorrectL           NoResponseRequired         IMRespond_Left   1              "IML-L"     IMResponseL;
   1970            NoResponseRequired      IMCorrectNR          NoResponseRequired         IMRespond_Right  2              "IMN-R"     IMResponseNR;
   1970            NoResponseRequired      IMCorrectNL          NoResponseRequired         IMRespond_Left   1              "IMN-L"     IMResponseNL;
   1970            NoResponseRequired      IMCorrectNo          NoResponseRequired         IMNo_Response    1              "IMNo-No"   IMResponseNo;
};   

#  The 5 Cues

TEMPLATE "Cue.tem" {
   ResponseTrialName    CueName           CueCode     CuePortCode    CueTrialName;
   IMResponseR          IMRespond_Right   " T 21"     21             IMCueR;
   IMResponseL          IMRespond_Left    " T 22"     22             IMCueL;
   IMResponseNR         IMRespond_Right   " T 23"     23             IMCueNR;
   IMResponseNL         IMRespond_Left    " T 24"     24             IMCueNL;
   IMResponseNo         IMNo_Response     " T 25"     25             IMCueNo; 
};

# The 5 Imagine Primes

TEMPLATE "IMPrime.tem" {
   CueTrialName      PrimeName         PrimeCode      PrimePortCode     PrimeTrialName;
   IMCueR            IMPrime_Right     " T 11"        11                IMPrimeR;
   IMCueL            IMPrime_Left      " T 12"        12                IMPrimeL;
   IMCueNR           IMPrime_Neutral   " T 13"        13                IMPrimeNR;
   IMCueNL           IMPrime_Neutral   " T 14"        14                IMPrimeNL;
   IMCueNo           IMPrime_Nogo      " T 15"        15                IMPrimeNo;  
};