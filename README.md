# testing_triggers
<h3>Here we test the latencies of triggers in the EEG room<h3>

<h4>Instructions for the recording computer:<h4>

//How to initialize communication with the eyetracker
1. In anaconda prompt:
conda activate eeg_eye #activating the environment
Jupyter notebook #opening the jupyter notebook
2. open the notebook et_lsl_recorder.ipynb


//How to initialize communication with the EEG

1. turn on the amplifier (purple) and the battery (black box on experimenter room) (
2. enter the eego software (make sure you see 'green' signals in the right bottom screen - showing communication with the amp)
3. go to "acquire"
4. choose a subject (or define one), and press next

//How to initialize communication with the LSL

1. enter the tobii_trigger_ttl.ipynb notebook
2. run all

//Record with LabRecorder
1. open the software LabRecorder
2. select the from the list of streams the one you want (usually all of them). if you don't see your streams press 'update'
3. change the file and location on the right according to the experiment, and start recording
4. start recording (on lab recorder)


<h4>Instructions for the stimulus computer:<h4>
  
//Record all triggers

1.Open the folder "C:\Users\admin\Desktop\Projects\Testing Triggers"
2.Open the script "main_testing_all_3_triggers.py"
3.Run the script (using the triangle button)
4.During the core.wait(15) update the LabRecorder software on the recording computer and start recording\

//Get data
1.Open the check_latencies_between_triggers or check_latencies_within_triggers script
2.Load the data using its file location string you defined in the LSL (LabRecorder)
3.Obtain the streams
4.Compare the latencies

-----
<b>CHANNELS ET<b>
('device_time_stamp', 1), # 0

    ('left_gaze_origin_validity',  1),  #1
    ('right_gaze_origin_validity',  1), #2

    ('left_gaze_origin_in_user_coordinate_system',  3), #3-5
    ('right_gaze_origin_in_user_coordinate_system',  3), #6-8

    ('left_gaze_origin_in_trackbox_coordinate_system',  3), #9-11
    ('right_gaze_origin_in_trackbox_coordinate_system',  3), #12-14

    ('left_gaze_point_validity',  1), #15
    ('right_gaze_point_validity',  1), #16

    ('left_gaze_point_in_user_coordinate_system',  3), #17-19
    ('right_gaze_point_in_user_coordinate_system',  3),#20-22

    ('left_gaze_point_on_display_area',  2), #23-24 (23-x_left, 24-y_left)
    ('right_gaze_point_on_display_area',  2), #25-26 (x-y of right eye)

    ('left_pupil_validity',  1), #27
    ('right_pupil_validity',  1), #28

    ('left_pupil_diameter',  1), #29
    ('right_pupil_diameter',  1) #30
