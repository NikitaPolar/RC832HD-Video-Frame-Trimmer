# RC832HD-Video-Frame-Trimmer

**Description:**
This Python script provides a solution for efficiently processing videos recorded with the RC832HD transmitter, removing frames predominantly matching a specific blue color. The problem often occurs during FPV video recordings when signal loss or other unexpected conditions result in extended periods of unwanted blue screens. Manual video editing can be time-consuming, and this tool automates the process.

**Features:**
- Removes frames mostly matching a user-specified blue color.
- Preserves the original frames and frames per second (FPS).
- Calculates and displays progress and estimated time remaining (ETA).

**How it Works:**
This script processes a video file, analyzes each frame, and identifies frames that are predominantly blue. These frames are removed, leaving a clean video with the same original FPS. The script calculates and displays progress, allowing users to track the completion status and ETA.

**Getting Started:**
- Clone or download the repository.
- Install required libraries (e.g., OpenCV).
- Run the script, specifying the input video file and desired output file.
