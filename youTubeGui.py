import PySimpleGUI as sg
import time
import os
import sys
import re
import yt_dlp

def main():
    # Step 1: Open the batch file
    batch_file_path = r"C:\Users\syarb\OneDrive\Desktop\youtubebatchfile\batchfileURL.txt"
    with open(batch_file_path, 'r') as file:
        urls = file.readlines()

    # Step 2: Show a progress bar
    progress_bar()

    # Step 3: Download and save the videos
    download_folder = r"C:\Users\syarb\OneDrive\Desktop\youtubedownloads"
    os.makedirs(download_folder, exist_ok=True)
    for url in urls:
        url = url.strip()  # Remove leading/trailing whitespaces and newlines
        download_video(url, download_folder)

    # Step 4: Print the name of each downloaded video
    print_video_names(download_folder)

    # Step 7: Print "You Have Run The Jewels ** Vandalize" in red color
    print("\033[91mYou Have Run The Jewels ** Vandalize\033[0m")

    # Step 8: Exit the program
    sys.exit(0)

def progress_bar():
    for _ in range(5):
        sys.stdout.write('\r')
        sys.stdout.write('[%-10s] %d%%' % ('='*_, 20*_))
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\n')

def download_video(url, download_folder):
    options = {
        'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
    }
    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])

def print_video_names(download_folder):
    for filename in os.listdir(download_folder):
        if filename.endswith('.mp4'):
            video_name = re.sub(r'\.mp4$', '', filename)  # Remove the file extension
            print(video_name)

# PySimpleGUI code
sg.theme('DarkRed1')  # Set the color theme

layout = [
    [sg.Button('Push', size=(10, 2), font=('Helvetica', 14), key='-PUSH-')]
]

window = sg.Window('Theivery Corp', layout, size=(270, 175), finalize=True)

while True:
    event, _ = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == '-PUSH-':
        main()

window.close()
