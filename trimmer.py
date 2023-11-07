import cv2
import numpy as np
import argparse
import time

# Function to check if a frame is mostly a specific blue color with increased sensitivity
def is_mostly_specific_blue(frame, blue_color):
    # Calculate the absolute difference between the frame and the specific blue color
    color_difference = np.abs(frame - blue_color)

    # Check if the frame is mostly blue based on the color difference
    is_blue = np.all(color_difference < 210, axis=2)

    return np.all(is_blue)

def format_eta(eta):
    hours, remainder = divmod(eta, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"

def process_video(input_video_path, output_video_path, blue_color):
    # Open the video file
    video_capture = cv2.VideoCapture(input_video_path)

    # Extract FPS information from the input video
    fps = int(video_capture.get(cv2.CAP_PROP_FPS))

    # Create a VideoWriter to save the trimmed video with the same FPS
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (int(video_capture.get(3)), int(video_capture.get(4))))

    # Read and process each frame
    frame_count = 0
    deleted_frames = 0
    total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))

    start_time = time.time()
    while video_capture.isOpened():
        ret, frame = video_capture.read()

        if not ret:
            break

        # Check if the frame is mostly the specific blue color
        if not is_mostly_specific_blue(frame, blue_color):
            out.write(frame)
        else:
            deleted_frames += 1

        # Calculate and display progress as a percentage
        frame_count += 1
        progress = int((frame_count / total_frames) * 100)
        elapsed_time = time.time() - start_time
        if frame_count > 0:
            estimated_total_time = elapsed_time / (frame_count / total_frames)
            eta = estimated_total_time - elapsed_time
        else:
            eta = 0
        formatted_eta = format_eta(eta)
        print(f"Processing: {progress}% complete | Deleted Frames: {deleted_frames} | ETA: {formatted_eta}", end="\r")

    # Release the video objects
    video_capture.release()
    out.release()

    cv2.destroyAllWindows()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process a video and remove frames mostly matching a specific blue color.')
    parser.add_argument('input_video', help='Path to the input video file')
    parser.add_argument('output_video', help='Path for the output video file')
    args = parser.parse_args()

    # Blue color in RGB format (#0401FF)
    blue_color = (255, 1, 4)

    process_video(args.input_video, args.output_video, blue_color)
