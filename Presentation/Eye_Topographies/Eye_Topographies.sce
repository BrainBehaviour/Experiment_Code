scenario = "Eye_Topographies_28/03/06";
default_font_size = 25;
pcl_file = "Eye_Topographies.pcl"; 
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
text{caption = "You will see a circle with a cross in the centre on the screen.\nKeeping your head still move your eyes to follow the circle.\n\nIf the circle is filled in white then blink your eyes.\n\nPress a button to see an example.";} IntroScreen;
text{caption = "Press a button when you are ready to start.";} IntroScreen2;
text{caption = "End of eye movements calibration.\n\nPress a button to exit.";} IntroScreen3;

# bitmaps
bitmap {filename = "open_circle_centre.bmp";} Open_Circle_Centre;						# T 5
bitmap {filename = "open_circle_left.bmp";} Open_Circle_Left;							# T 6
bitmap {filename = "open_circle_right.bmp";} Open_Circle_Right;     					# T 7
bitmap {filename = "open_circle_top.bmp";} Open_Circle_Top;							   # T 8
bitmap {filename = "open_circle_bottom.bmp";} Open_Circle_Bottom; 			  		# T 9
bitmap {filename = "filled_circle_centre.bmp";} Filled_Circle_Centre;				# T 10

# Main trials

TEMPLATE "Stim.tem" {
   BitmapName    				Code     PortCode    TrialName;
   Open_Circle_Centre		" T 5"	5				OpenCircleCentre;
   Open_Circle_Left			" T 6"	6				OpenCircleLeft;
   Open_Circle_Right			" T 7"	7				OpenCircleRight;
   Open_Circle_Top			" T 8"	8				OpenCircleTop;
   Open_Circle_Bottom		" T 9"	9				OpenCircleBottom;
   Filled_Circle_Centre		" T 10"	10				FilledCircleCentre;
};    
     
#Introduction Code  

TEMPLATE "IntroScreen.tem" {   
   stext           scode             IntroName;
   IntroScreen     "Intro Screen"	 Intro1;
   IntroScreen2    "Intro Screen 2"  Intro2;
   IntroScreen3	 "Intro Screen 3"  Intro3;
};

