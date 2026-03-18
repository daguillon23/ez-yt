import subprocess as sb
from pathlib import Path

def run(args, link, output=False):
    # EXPECTED INPUT
    # args[0]: "yt-dlp". runs executable
    # args[1]: "-t". flag that automates file conversion
    # args[2]: "mp3". for audio
    # link: {YT link to song or playlist}
    # output: denotes whether output flag activated

    # OPTIONAL
    # args[3]: "-o". specifies output modification
    # args[4]: {path string}. formats songs by track num and title

    try:
        # SUBPROCESS FLAGS
        # check: throws exception for errors
        # capture_output: stores output in result
        # text: stores output as Strings instead of bytes
        # shell: DANGEROUS; spins up new shell, takes one string as args
        run_args = [args[0], args[1], args[2], link]
        if output:
            run_args.append(args[3])
            run_args.append(args[4])
        result = sb.run(run_args, check=True, capture_output=True, text=True)
        print(result.stdout)
    except sb.CalledProcessError as e:
        print(f"ERROR: {e.cmd} returned {e.returncode}")
        print(f"out: {e.stdout}")
        print(f"err: {e.stderr}")

def download(input):
    # EXPECTED INPUT
    # input[0]: artist name
    # input[1]: album name
    # input[2]: link to YT playlist of album songs
    ARTIST = input[0]
    ALBUM = input[1]
    LINK = input[2]
    path = f"./Music/{ARTIST}/{ALBUM}"

    # PATH FLAGS
    # parents: creates missing parent directories
    # exist_ok: prevents error if directory already exists
    # this line ensures that directory exists for yt-dlp to download files into
    Path(path).mkdir(parents=True, exist_ok=True)

    TYPE = "mp3"
    
    # YT-DLP VARS
    # playlist_index: keeps track of number that downloaded file is in playlist
    # title: title of downloaded file
    # ext: downloaded file's extension
    args = ["yt-dlp","-t", f"{TYPE}", "-o", f"{path}/%(playlist_index)02d %(title)s.%(ext)s"]
    output = True
    run(args, LINK, output)
    
def main():
    # EXPECTED INPUT
    # input.txt should have 3 lines
    # line 1: artist name
    # line 2: album name
    # line 3: YT link
    fpath = "input.txt"
    input = []
    with open(fpath) as f:
        for line in f:
            strip = line.strip()
            input.append(strip)
            print(strip)
    download(input)