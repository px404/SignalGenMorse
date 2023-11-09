# Error: \pydub\utils.py", line 170
#    warn("Couldn't find ffmpeg or avconv - defaulting to ffmpeg, but may not work", RuntimeWarning)

## Info:

FFmpeg is the leading multimedia framework, able to decode, encode, transcode, mux, demux, stream, filter and play pretty much anything that humans and machines have created. It supports the most obscure ancient formats up to the cutting edge.
~ https://blog.gregzaal.com/how-to-install-ffmpeg-on-windows/

## Solution:
https://www.ffmpeg.org/
Download (not source code, download a prebuilt installer or the exe version from the site)

Unzip - download a tool like .7zip it makes it easier to compress and decompress files

Add it to PATH

	EDIT SYSTEM ENVIRONMENT VARIABLES
	System Variables (NOT user variables)
	PATH
	NEW
	Paste the address for ffmpeg.exe folder after moving the folder to someplace safe
	(It should be something like C:/ffmpeg/bin)

If it doesn't work, Google it or chatGPT it whichever is of the preferred methods to figure out things that are like this.
