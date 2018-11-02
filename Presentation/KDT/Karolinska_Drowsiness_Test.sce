scenario = "Karolinska_Drowsiness_Test_25/10/07";
default_font_size = 25;
pcl_file = "Karolinska_Drowsiness_Test.pcl"; 
default_font = "Arial"; 
default_text_color = 0,0,0;
default_all_responses = false;
default_background_color = 255,255,255; 
active_buttons = 4;
button_codes = 1,2,3,4;
response_matching = simple_matching;
write_codes = true;
pulse_width = 20;
begin;                
picture {} default;

#Introduction Screen
text{caption = "You will see a black circle on a white screen.\n\nKeeping your head still and your body relaxed and still,\nfocus on the circle until it disappears.\n\nPress a button when you are ready to start.";} IntroScreen;
text{caption = "End of Karolinska Drowsiness Test.\n\nPress a button to exit.";} IntroScreen2;

# bitmaps
bitmap {filename = "open_circle_centre3.bmp";} Open_Circle_Centre;

#Introduction Code  

TEMPLATE "IntroScreen.tem" {   
   stext           scode             IntroName;
   IntroScreen     "Intro Screen"	 Intro1;
   IntroScreen2    "Intro Screen 2"  Intro2;
};

trial{
      trial_duration = 120000;
      trial_type = first_response;          
      
      picture{
            bitmap Open_Circle_Centre;
            x = 0; y = 0;
      };
      deltat = 0;
      duration = 120000; 

      code = "T 5";
		port_code = 5;
      
}OpenCircleCentre; 