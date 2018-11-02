scenario = "Behavioural_Nogo2_11/11/04";
default_font_size = 25;
pcl_file = "Behavioural_Nogo2_Main.pcl"; 
default_font = "Arial";
default_all_responses = false;
default_background_color = 0,0,0; 
active_buttons = 4;
button_codes = 1,2,3,4;
response_matching = simple_matching;
write_codes = true;
pulse_width = 20;
begin;                
picture {} default;  

#Introduction Screen
text{caption = "In each trial you will first see a circle\nthen a pair of arrows will quickly flash inside this circle\nThese arrows tell you how to prepare for the forthcoming response\n\n>> Right hand\n<< Left hand\n>< NO Response required\n\nAfter a short delay, half of the circle will become white\nThis tell you which button to press\n\nRight Button = Right half of circle lit\nLeft Button = Left half of circle lit\nNO Response = Bottom half of the circle will be lit\n\nPress a button to start training trials";} IntroScreen;

#Training Screen
text{caption = "In this training block you will practice\n\nLeft <<\n\nand\n\nRight >>\n\ntrials only\n\nThe arrows mean get ready to respond with the appropriate hand\n\nPress a button to continue";}TrainScreen1; 
#text{caption = "In this training block you will practice\n\nNeutral <>\n\ntrials only\n\nThe arrows mean get ready to respond with either hand\n\nPress a button to continue";}TrainScreen2;
text{caption = "In this training block you will practice\n\nNo-response ><\n\ntrials only\n\nThe arrows mean you do not need to prepare to respond\n\nPress a button to continue";}TrainScreen3;
text{caption = "Rarely, the arrows will not predict the\nforthcoming response\n\nWe will practice these now\n\nPress a button to continue";}TrainScreen4;

# Open circle
bitmap {filename = "Open Circle.bmp";} Open_Circle;
  
#Primes
bitmap {filename = "PrimeRight.bmp";} Prime_Right;    # R-Valid T 11; R-Left T 13; R-No Response T 21

bitmap {filename = "PrimeLeft.bmp";} Prime_Left;      # L-Valid T 12; L-Right T 14; L-No Response T 22

#bitmap {filename = "PrimeNeutral.bmp";} Prime_Neutral;# Ne-Right T 15; Ne-Left T 16; Ne-No Response T 20

bitmap {filename = "PrimeNo.bmp";} Prime_Nogo;        # No-Valid T 17; No-Right T 18; No-Left T 19

#text{caption = ">>";
     #font_size = 40;
   #}Prime_Right;   # T 11
#text{caption = "<<";
     #font_size = 40;
   #}Prime_Left;    # T 12
#text{caption = "<>";
     #font_size = 40;
   #}Prime_Neutral; # T 13
#text{caption = "><";
     #font_size = 40;
   #}Prime_Nogo;    # T 14
   
#Cues  
bitmap {filename = "Right Response.bmp";} Respond_Right; # Right-R T 30; Left-R T 33; Neutral-R T 34;No Response-R T 37

bitmap {filename = "Left Response.bmp";} Respond_Left;   # Left-L T 31; Right-L T 32; Neutral-L T 35; No Response-L T 38 

bitmap {filename = "No Response.bmp";} No_Response;      # No Response-No T 36; Right-No T 40; Left-No T 41; Neutral-No T 39

#text{caption = "RH";
     #font_size = 40;
   #}Respond_Right; #  Right Valid  T 20       
#text{caption = "LH";
     #font_size = 40;
   #}Respond_Left;  #  Left Valid   T 21       Neutral Right  T 22
#text{caption = "NO";
     #font_size = 40;
   #}No_Response;   #  Nogo Valid   T 24       Neutral Left   T 23

#Response Feedback
text{caption = "Correct";           # Right Button Press Correct: Right-R T 50; Left-R T 53; Neutral-R T 54; No Response-R T 57
     font_size = 40;                # Left Button Press Correct:  Left-L T 51; Right-L T 52; Neutral-L T 55; No Response-L T 58
     font_color = 0,255,0;          # No Response Correct:  No Response-No T 56; Right-No T 60; Left-No T 61; Neutral-No T 59  
     }Correct;                           
                                     
    
                                    

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

text{caption = "!! Please take a break !!\nExperiment has been paused by the experimenter";}Pause;    # T 85
text{caption = "When you are ready to continue press a button";}Continue;     

text{caption = "End of Block:";}Block;               # T 80
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
     port_code = 85;
     
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
     port_code = 80;  
     
}EndTrial; 


# Feedback 

TEMPLATE "Feedback.tem" {
   Feedback    FeedbackCode      FeedbackPortCode     FeedbackName;
   Correct     " T 50"           50                   CorrectR_R;
   Correct     " T 51"           51                   CorrectL_L;
   Correct     " T 52"           52                   CorrectR_L;
   Correct     " T 53"           53                   CorrectL_R;
  #Correct     " T 54"           54                   CorrectN_R;
  #Correct     " T 55"           55                   CorrectN_L;
   Correct     " T 56"           56                   CorrectNo_No;
   Correct     " T 57"           57                   CorrectNo_R;
   Correct     " T 58"           58                   CorrectNo_L;
  #Correct     " T 59"           59                   CorrectN_No;
  #Correct     " T 60"           60                   CorrectR_No;
  #Correct     " T 61"           61                   CorrectL_No;
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
  #TrainScreen2   "Train Screen 2"  Intro4;
   TrainScreen3   "Train Screen 3"  Intro5;
   TrainScreen4   "Train Screen 4"  Intro6;
   Pretrial       "Pretrial"        Intro7; 
};


#  The 12 Responses

TEMPLATE "Response.tem" {
   trialduration   WrongFeedbackTrialName  NoFeedbackTrialName  CorrectFeedbackTrialName   CueName        ButtonNumber   CueCode  ResponseTrialName;
   2600		       FeedbackWrong           Responserequired     CorrectR_R                 Respond_Right  2              "R-R"    ResponseR_R;
   2600            FeedbackWrong           Responserequired     CorrectL_L                 Respond_Left   1              "L-L"    ResponseL_L;
   2600            FeedbackWrong           Responserequired     CorrectR_L                 Respond_Left   1              "R-L"    ResponseR_L;
   2600            FeedbackWrong           Responserequired     CorrectL_R                 Respond_Right  2              "L-R"    ResponseL_R;
  #1600            FeedbackWrong           Responserequired     CorrectN_R                 Respond_Right  2              "N-R"    ResponseN_R;
  #1600            FeedbackWrong           Responserequired     CorrectN_L                 Respond_Left   1              "N-L"    ResponseN_L;
   2600            NoResponseRequired      CorrectNo_No         NoResponseRequired         No_Response    1              "No-No"  ResponseNo_No;
   2600            FeedbackWrong           Responserequired     CorrectNo_R                Respond_Right  2              "No-R"   ResponseNo_R;
   2600	          FeedbackWrong           Responserequired     CorrectNo_L                Respond_Left   1              "No-L"   ResponseNo_L;
  #1600            NoResponseRequired      CorrectN_No          NoResponseRequired         No_Response    1              "N-No"   ResponseN_No;
  #1600            NoResponseRequired      CorrectR_No          NoResponseRequired         No_Response    1              "R-No"   ResponseR_No;
  #1600            NoResponseRequired      CorrectL_No          NoResponseRequired         No_Response    1              "L-No"   ResponseL_No;
};                                                                                                                
                                                                                                                  
#  The 12 Cues

TEMPLATE "Cue.tem" {
   ResponseTrialName CueName        CueCode  CuePortCode CueTrialName;
   ResponseR_R       Respond_Right  " T 30"   30          CueR_R;
   ResponseL_L       Respond_Left   " T 31"   31          CueL_L;
   ResponseR_L       Respond_Left   " T 32"   32          CueR_L;
   ResponseL_R       Respond_Right  " T 33"   33          CueL_R;
  #ResponseN_R       Respond_Right  " T 34"   34          CueN_R;
  #ResponseN_L       Respond_Left   " T 35"   35          CueN_L;
   ResponseNo_No     No_Response    " T 36"   36          CueNo_No;
   ResponseNo_R      Respond_Right  " T 37"   37          CueNo_R;
   ResponseNo_L      Respond_Left   " T 38"   38          CueNo_L;
  #ResponseN_No      No_Response    " T 39"   39          CueN_No;
  #ResponseR_No      No_Response    " T 40"   40          CueR_No;
  #ResponseL_No      No_Response    " T 41"   41          CueL_No; 
};

# The 12 Primes

TEMPLATE "Prime.tem" {
   CueTrialName      PrimeName     PrimeCode  PrimePortCode PrimeTrialName;
   CueR_R            Prime_Right   " T 11"    11            PrimeR_R;
   CueL_L            Prime_Left    " T 12"    12            PrimeL_L;
   CueR_L            Prime_Right   " T 13"    13            PrimeR_L;
   CueL_R            Prime_Left    " T 14"    14            PrimeL_R;
  #CueN_R            Prime_Neutral " T 15"    15            PrimeN_R;
  #CueN_L            Prime_Neutral " T 16"    16            PrimeN_L;
   CueNo_No          Prime_Nogo    " T 17"    17            PrimeNo_No;
   CueNo_R           Prime_Nogo    " T 18"    18            PrimeNo_R;
   CueNo_L           Prime_Nogo    " T 19"    19            PrimeNo_L;
  #CueN_No           Prime_Neutral " T 20"    20            PrimeN_No;
  #CueR_No           Prime_Right   " T 21"    21            PrimeR_No;
  #CueL_No           Prime_Left    " T 22"    22            PrimeL_No;  
};

