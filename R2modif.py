# Import librairies
import os
import datetime

# Function that extract the 'modified timestamp' from the video file
def extract_modified_datetime(filepath):
    modified_timestamp = os.path.getmtime(filepath)
    modified_datetime = datetime.datetime.fromtimestamp(modified_timestamp)
    return modified_datetime

# Function to rename the video file in the format 'yyyymmdd HHMMSS.mp4' - ie: '20230518 150759.mp4'
def rename_video_with_modified_datetime(filepath):
    dirname = os.path.dirname(filepath)
    filename = os.path.basename(filepath)

    modified_datetime = extract_modified_datetime(filepath)
    new_filename = modified_datetime.strftime("%Y%m%d %H%M%S") + os.path.splitext(filename)[1]
    new_filepath = os.path.join(dirname, new_filename)

    os.rename(filepath, new_filepath)
    print(f"Renamed '{filename}' to '{new_filename}'")

# Get the current directory
current_directory = os.getcwd()

# Get a list of all files in the current directory
files = os.listdir(current_directory)

# Go through the list, Extract the 'modified timestamp' and Rename the file accordingly
for file in files:
    if file.endswith(".mp4"):
        file_path = os.path.join(current_directory, file)
        rename_video_with_modified_datetime(file_path)

