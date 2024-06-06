import os
import cv2
from flask import current_app


def generate_thumbnail(video_path):
    # Open the video file
    video = cv2.VideoCapture(video_path)

    # Read the first frame
    ret, frame = video.read()

    filename = os.path.basename(video_path)  # '/path/to/video/video_{upload_id}_{video}.mp4' - original path
    filename_without_prefix = filename.split('_', 1)[-1] # '/path/to/video/{upload_id}_{video}.mp4' - remove "video_"
    filename_without_extension = os.path.splitext(filename_without_prefix)[0]  # '/path/to/video/{upload_id}_{video}' - remove video format
    thumbnail_filename = f"thumbnail_{filename_without_extension}.jpg" # '/path/to/video/thumbnail_{upload_id}_{video}.jpg' - add thumbnail formatting

    thumbnail_path = os.path.join(current_app.config['UPLOAD_THUMBNAILS_PATH'], thumbnail_filename)

    # Save the first frame as the thumbnail
    cv2.imwrite(thumbnail_path, frame)

    # Release the video capture object
    video.release()

    return thumbnail_path