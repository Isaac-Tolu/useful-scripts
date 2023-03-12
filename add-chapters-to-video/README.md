# add-chapters-to-video
I was watching a long video course with VLC. There were chapters for the video and I needed to add these chapters into VLC so I can better organise my watching of the video. I searched online for solutions and I was able to get this.

## Credits
The main [blog](https://ikyle.me/blog/2020/add-mp4-chapters-ffmpeg) I got the solution from.

## Requirements
- A Linux machine. I did everything on an Ubuntu Linux machine, and I'm yet to test it out on Mac or Windows. 
- [ffmpeg](https://ffmpeg.org/) - A command line utility for processing of audio and video files
- Python, of course!! But, you can convert the Python code to any language of your choice.

# Usage
- Create a `chapters.txt` [file](./chapters.txt) with each chapter timestamp and title on a different line in this format:
```
00:00:00 Chapter1
00:25:53 Chapter2
00:52:49 Chapter3
02:25:44 Chapter4
03:55:21 Chapter5
```
- Extract the metadata from the video file into a [file](./FFMETADATAFILE.txt) called `FFMETADATAFILE.txt`
```
ffmpeg -i <INPUT_VIDEO_FILE> -f ffmetadata FFMETADATAFILE.txt
```
- The metadata file should show that there are no chapters in the video and it should be like this
```
;FFMETADATA1
major_brand=mp42
minor_version=0
compatible_brands=isommp42
encoder=Lavf58.76.100
```
- Run the python [code](./parse_chapters.py) which parses the chapters from and puts it in the metadata file in the required format
```
python parse_chapters.py
```
- Look at the metadata [file](./FFMETADATAFILE.txt) to see the format of the new chapters
- Create a new video file that copies video and audio from the original video but uses the modified metadata file that the python code returns
```
ffmpeg -i <INPUT_VIDEO_FILE> -i FFMETADATAFILE -map_metadata 1 -codec copy <OUTPUT_VIDEO_FILE>
```
- Open the output video file to confirm that chapters have now been added