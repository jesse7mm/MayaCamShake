# change "camera1" on line 27 to the name of the renderable camera in your scene if you are not using the default camera
# you need to have at least two keyframes to add shake or you will get a warning
import maya.cmds as cmds
import random

def add_continuous_camera_shake(camera_name, duration, intensity, frequency_range):
    num_keyframes = cmds.keyframe(camera_name, query=True, attribute=['translateX', 'translateY', 'translateZ'], keyframeCount=True)

    if num_keyframes < 2:
        cmds.warning("The selected camera has less than 2 keyframes. Camera shake cannot be applied.")
        return

    for frame in range(1, duration + 1):
        # Check if the current frame is within the frequency range
        if frame % random.randint(frequency_range[0], frequency_range[1]) == 0:
            random_translation = [random.uniform(-intensity, intensity) for _ in range(3)]
            animated_frame = frame % num_keyframes if frame % num_keyframes != 0 else num_keyframes
            
            for axis, translation in zip(['X', 'Y', 'Z'], random_translation):
                current_translation = cmds.keyframe(camera_name, query=True, attribute='translate' + axis, time=(animated_frame, animated_frame))

                if current_translation:
                    new_translation = current_translation[0] + translation
                    cmds.setKeyframe(camera_name, attribute='translate' + axis, time=(animated_frame, animated_frame), value=new_translation)

# Set the camera name (change to your camera's name)
camera_name = "camera1"

# Set the total duration of the camera shake
duration = 240  # Total number of frames for the shake

# Set the intensity of the camera shake
intensity = 0.5  # Maximum translation in any direction

# Set the frequency range for the shake (between 3 and 10 frames)
frequency_range = (3, 10)

# Call the function to add continuous camera shake to the animated camera
add_continuous_camera_shake(camera_name, duration, intensity, frequency_range)
