import subprocess, sys
# Write your program below

#url = "YOUTUBE-URL"

command1 = "yt-dlp -x"\
                + " --audio-quality 0 --audio-format mp3 "\
                + " -o '%(title)s.%(ext)s'"\
                + " --restrict-filenames"\
                + " --quiet "\
                + url
status = subprocess.run(command1, capture_output=True, shell=True)

if status.returncode != 0:
    print("Failed to download/save " + url)

fileName = "sample"
command2 = "yt-dlp -x"\
                + " --audio-quality 0 --audio-format mp3 "\
                + " -o '" + fileName + ".%(ext)s'"\
                + " --restrict-filenames"\
                + " --quiet "\
                + url
status = subprocess.run(command2, capture_output=True, shell=True)

if status.returncode != 0:
    print("Failed to download/save " + fileName)

