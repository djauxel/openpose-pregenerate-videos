import os
from pregenerate import pregenerate_command

# Change directory to where OpenPose is installed on your computer
os.chdir('C:\\Projects\\openpose')

# Modify these paths to where this repository is located on your computer
# input_video_dir = C:\...\openpose-pregenrate-videos\videos
# output_video_dir = C:\...\openpose-pregenrate-videos\openpose_output\openpose_output\videos
# output_json_dir = C:\...\openpose-pregenrate-videos\openpose_output\openpose_output\json
input_video_dir = 'C:\\Projects\\openpose-pregenerate-videos\\videos'
output_video_dir = 'C:\\Projects\\openpose-pregenerate-videos\\openpose_output\\videos'
output_json_dir = 'C:\\Projects\\openpose-pregenerate-videos\\openpose_output\\json'

# Change MAX_VIDEOS to the amount of videos you will be processing
MAX_VIDEOS = 500
count = 0

for file in os.listdir(input_video_dir):
    count += 1
    print('\nPROCESSING {} OF {}'.format(count, MAX_VIDEOS))
    if file.endswith('.mp4') or file.endswith('.avi'):
        os.system('cmd /c' + pregenerate_command(file, input_video_dir, output_video_dir, output_json_dir))
    else:
        print('Unable to process video. {}\'s file format is not supported.'.format(file))

print('\nFINISHED PROCESSING VIDEOS')