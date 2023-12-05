def reduce(inPath, filename, outPath):
    import numpy as np
    import cv2
    from moviepy.editor import VideoFileClip

    # Replace with the path to your video file
    video_file_path = inPath + "/" + filename

    # Load the video file using moviepy
    clip = VideoFileClip(video_file_path)

    # Apply noise reduction to each frame in the video
    def apply_noise_reduction(image):
        image = np.array(image)
        reduced_noise_image = cv2.fastNlMeansDenoising(image, None, 10, 7, 21)
        return reduced_noise_image

    noise_reduced_clip = clip.fl_image(apply_noise_reduction)

    # Save the output video
    noise_reduced_clip.write_videofile(outPath + "/2" + filename)
