scenario = "Nogo3_11/11/04";
default_font_size = 25;
pcl_file = "Nogo3_Main.pcl"; 
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
text{caption = "In each trial you will first see a circle\nthen a pair of arrows will quickly flash inside this circle\nThese arrows tell you how to prepare for the forthcoming response\n\n>> Right hand\n<< Left hand\n<> Right or Left hand\n>< NO Response required\n\nAfter a short delay, half of the circle will become white\nThis tell you which button to press\n\nRight Button = Right half of circle lit\nLeft Button = Left half of circle lit\nNO Response = Bottom half of the circle will be lit\n\nPress a button to start training trials";} IntroScreen;

#Training Screen
text{caption = "In this training block you will practice\n\nLeft <<\n\nand\n\nRight >>\n\ntrials only\n\nThe arrows mean get ready to respond with the appropriate hand\n\nPress a button to continue";}TrainScreen1; 
text{caption = "In this training block you will practice\n\nNeutral <>\n\ntrials only\n\nThe arrows mean get ready to respond with either hand\n\nPress a button to continue";}TrainScreen2;
text{caption = "In this training block you will practice\n\nNo-response ><\n\ntrials only\n\nThe arrows mean you do not need to prepare to respond\n\nPress a button to continue";}TrainScreen3;

# Open circle
bitmap {filename = "Open Circle.bmp";} Open_Circle;
  
#Precues
bitmap {filename = "PrecueRight.bmp";} Precue_Right;    # T 11

bitmap {filename = "PrecueLeft.bmp";} Precue_Left;      # T 12

bitmap {filename = "PrecueNeutral.bmp";} Precue_Neutral;# Right T 13; Left T 14

bitmap {filename = "PrecueNo.bmp";} Precue_Nogo;        # T 15

   
#Cues  
bitmap {filename = "Right Response.bmp";} Respond_Right; # Right T 20, Neutral T 22

bitmap {filename = "Left Response.bmp";} Respond_Left;   # Left T 21, Neutral T 23

bitmap {filename = "No Response.bmp";} No_Response;      # T 24


#Response Feedback
text{caption = "Correct";           #  Right Valid       T 30
     font_size = 40;                #   Left Valid       T 31
     font_color = 0,255,0;          #   Neutral Right    T 32   
     }Correct;                      #   Neutral Left     T 33     
                                    #   Nogo Valid       T 34 
    
                                    

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
   Correct     " T 30"           30                   CorrectR;
   Correct     " T 31"           31                   CorrectL;
   Correct     " T 32"           32                   CorrectNR;
   Correct     " T 33"           33                   CorrectNL;
   Correct     " T 34"           34                   CorrectNo;                    
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
   trialduration   WrongFeedbackTrialName  NoFeedbackTrialName  CorrectFeedbackTrialName   CueName        ButtonNumber   CueCode  ResponseTrialName;
   2670            FeedbackWrong           Responserequired     CorrectR                   Respond_Right  2              "R-R"    ResponseR;
   2670            FeedbackWrong           Responserequired     CorrectL                   Respond_Left   1              "L-L"    ResponseL;
   2670            FeedbackWrong           Responserequired     CorrectNR                  Respond_Right  2              "N-R"    ResponseNR;
   2670            FeedbackWrong           Responserequired     CorrectNL                  Respond_Left   1              "N-L"    ResponseNL;
   2670            NoResponseRequired      CorrectNo            NoResponseRequired         No_Response    1              "No-No"  ResponseNo;
};   

#  The 5 Cues

TEMPLATE "Cue.tem" {
   ResponseTrialName CueName        CueCode  CuePortCode CueTrialName;
   ResponseR         Respond_Right  " T 20"   20          CueR;
   ResponseL         Respond_Left   " T 21"   21          CueL;
   ResponseNR        Respond_Right  " T 22"   22          CueNR;
   ResponseNL        Respond_Left   " T 23"   23          CueNL;
   ResponseNo        No_Response    " T 24"   24          CueNo; 
};

# The 5 Precues

TEMPLATE "Precue.tem" {
   CueTrialName      PrecueName     PrecueCode  PrecuePortCode PrecueTrialName;
   CueR              Precue_Right   	" T 11"     11             PrecueR;
   CueL              Precue_Left    	" T 12"     12             PrecueL;
   CueNR             Precue_Neutral 	" T 13"     13             PrecueNR;
   CueNL             Precue_Neutral 	" T 14"     14             PrecueNL;
   CueNo             Precue_Nogo    	" T 15"     15             PrecueNo;  
};

