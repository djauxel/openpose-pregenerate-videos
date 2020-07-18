import os

def pregenerate_command(input_video_file, input_video_dir, output_video_dir, output_json_dir):
    file_name = os.path.splitext(input_video_file)

    input_video_path = '\"' + input_video_dir + '\\' + file_name[0] + '.mp4' + '\"'
    output_video_path = '\"' + output_video_dir + '\\' + input_video_file + '\"'
    output_json_path = '\"' + output_json_dir + '\\' + file_name[0] + '.json' + '\"'

    # Separate the command into parts
    openpose_build_dir = 'build\\x64\\Release\\OpenPoseDemo.exe'
    input_video = '--video ' + input_video_path
    openpose_options = '--hand --face --disable_blending --display 0 --number_people_max 1'
    output_video = '--write_video ' + output_video_path
    output_json = '--write_json ' + output_json_path

    return build_full_command(openpose_build_dir, input_video, openpose_options, output_video, output_json)

def build_full_command(openpose_build_dir, input_video, openpose_options, output_video, output_json):
    command_parts = []
    command_parts.append(openpose_build_dir)
    command_parts.append(input_video)
    command_parts.append(openpose_options)
    command_parts.append(output_video)
    command_parts.append(output_json)

    full_command = ' '.join(command_parts)

    return full_command