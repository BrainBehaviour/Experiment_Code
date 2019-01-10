response_matching = simple_matching;
active_buttons = 2;
default_font_size = 0.6;

default_font = "Arial";

no_logfile = false;

# screen dimensions in pixels

screen_width = 1280;
screen_height = 1024;

screen_bit_depth = 32;

screen_width_distance = 38;
screen_height_distance = 30;

screen_distance = 60;

pcl_file = "percp load.pcl";
begin;

# instructions
text{caption = "blah"; font_color = 255,255,255;}instr_text;

# break
text{caption = "Please take a break \n\n press a response button when ready to continue"; font_color = 255,255,255;}break_text;

# end
text{caption = "End of Experiment\n\nThankyou for your time : )"; font_color = 255,255,255;}end_text;

# targets
text{caption = "X"; font_color = 255,255,255;}X;
text{caption = "N"; font_color = 255,255,255;}N;

text{caption = "blah"; font_color = 255,255,255;}flanker;
# low load distracter
text{caption = "O"; font_color = 255,255,255;}O;
# high load distracters
text{caption = "K"; font_color = 255,255,255;}K;
text{caption = "M"; font_color = 255,255,255;}M;
text{caption = "Z"; font_color = 255,255,255;}Z;
text{caption = "W"; font_color = 255,255,255;}W;
text{caption = "H"; font_color = 255,255,255;}H;
text{caption = "V"; font_color = 255,255,255;}V;
text{caption = "Y"; font_color = 255,255,255;}Y;

# neutral flanker
text{caption = "L"; font_color = 255,255,255;}L;

text{caption = "+"; font_color = 255,255,255;}fix;
arrow_graphic {coordinates = -15, 0, 15, 0; line_width = 0.1; head_width =0.5 ; head_length = 0.5;head_type = head_swift;}arrow;

trial{
trial_type = fixed;
trial_duration = 1000;

	picture{
	text fix;
	x = 0;
	y = 0;
	}no_cue_fix_pic;
	
	code = "no_cue_fix";
	
}no_cue_fix_trial;

trial{
trial_type = fixed;
trial_duration = 1000;

	picture{
	text fix;
	x = 0;
	y = 0;
	}cue_fix_pic;
	
	time = 0;
	duration = 800;
	
	picture{
	arrow_graphic arrow;
	x = 0;
	y = 0;
	}cue_fix_arrow;
	time = 800;
	duration = 200;
	
	code = "cue_fix";
	
}cue_fix_trial;


trial{
trial_type = first_response;
trial_duration = 3500;
	
	stimulus_event{
	
		picture{
		}letter_pic;
		
	}letter_event;
	
}letter_trial;

# instructions trial to be shown before the long trials
trial{
trial_type = first_response;
trial_duration = forever;

	picture{
	text instr_text;
	x=0;
	y=0;
	};
	
}instr_trial;

# break trial
trial{
trial_type = first_response;
trial_duration = forever;

	picture{
	text break_text;
	x=0;
	y=0;
	};
	
}break_trial;

# instructions trial to be shown before the long trials
trial{
trial_type = fixed;
trial_duration = 5000;

	picture{
	text break_text;
	x=0;
	y=0;
	};
	
}break_trial_fixed;

# end of experiment trial

trial{
trial_type = fixed;
trial_duration = 1000000;

	picture{
	text end_text;
	x=0;
	y=0;
	};
	
}end_trial;
