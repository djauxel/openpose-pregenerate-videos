# openpose-pregenerate-videos

### What does this script do?
In short, this script automates the process of having to type the command below. The command uses the [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) software to pregenerate a video of a stick figure on a black background.

```build\x64\Release\OpenPoseDemo.exe --video "C:\Projects\openpose-pregenerate-videos\videos" --hand --face --disable_blending --display 0 --number_people_max 1 --write_video "C:\Projects\openpose-pregenerate-videos\openpose_output\videos\output_video.avi" --write_json "C:\Projects\openpose-pregenerate-videos\openpose_output\json\output_keypoints.json"```

Can you imagine typing this command for every video that you plan on pregenerating? Neither can I!

### Explanation of .gitignore
In the .gitignore, I am ignoring all files within ```\videos```, ```\openpose_output\videos```, and ```\openpose_output\json``` with an exception. The exception is that any .gitkeep file will not be ignored. This is done so that I can upload the empty folders to GitHub, which the script requires. **Before running the script**, be sure to delete the .gitkeep files from the 3 directories, otherwise the script won't work.