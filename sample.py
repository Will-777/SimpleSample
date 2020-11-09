from pydub import AudioSegment
from pydub.playback import play


# according Song/audio files, you might need to change the type file.
"""
song = AudioSegment.from_wav("never_gonna_give_you_up.wav")
...or a mp3

song = AudioSegment.from_mp3("never_gonna_give_you_up.mp3")
... or an ogg, or flv, or anything else ffmpeg supports

ogg_version = AudioSegment.from_ogg("never_gonna_give_you_up.ogg")
flv_version = AudioSegment.from_flv("never_gonna_give_you_up.flv")

mp4_version = AudioSegment.from_file("never_gonna_give_you_up.mp4", "mp4")
wma_version = AudioSegment.from_file("never_gonna_give_you_up.wma", "wma")
aac_version = AudioSegment.from_file("never_gonna_give_you_up.aiff", "aac")
"""
sample1 = AudioSegment.from_file("06EmCallsPaul.m4a", "m4a")

#Slicing audio:
"""
# pydub does things in milliseconds
ten_seconds = 10 * 1000
first_10_seconds = song[:ten_seconds]
last_5_seconds = song[-5000:]

"""

#Save the results (again whatever ffmpeg supports)
"""
awesome.export("mashup.mp3", format="mp3")
Save the results with tags (metadata)

awesome.export("mashup.mp3", format="mp3", tags={'artist': 'Various artists', 'album': 'Best of 2011', 'comments': 'This album is awesome!'})
You can pass an optional bitrate argument to export using any syntax ffmpeg supports.

awesome.export("mashup.mp3", format="mp3", bitrate="192k")
Any further arguments supported by ffmpeg can be passed as a list in a 'parameters' argument, with switch first, argument second. Note that no validation takes place on these parameters, and you may be limited by what your particular build of ffmpeg/avlib supports.

# Use preset mp3 quality 0 (equivalent to lame V0)
awesome.export("mashup.mp3", format="mp3", parameters=["-q:a", "0"])

# Mix down to two channels and set hard output volume
awesome.export("mashup.mp3", format="mp3", parameters=["-ac", "2", "-vol", "150"])

"""
# Shong name

audioFileName = "06EmCallsPaul.m4a"
sample1 = AudioSegment.from_file(audioFileName, "m4a")
print("Input the song name (done) : {}".format(audioFileName))

# input the beginning of the sample
sample1_Begin = float(input("input the beginning of the sample in seconds \n(for more precision you can use float like 3.62)) : ")) * 1000
# input the end of the sample
sample1_End = float(input("input the End of the sample in seconds \n(for more precision you can use float like 3.62)) : ")) * 1000


# Create the sample
sample1 = sample1[sample1_Begin:sample1_End]


# duration of the sample & buggy play
print("New longer of the audio file : {} sec.".format(sample1.duration_seconds ))
print("Play doesn't work yet due to reading permission on temporary file.")
#play(sample1)

# input Sample name
sample_name = input("input the name of the sample (no need to add .mp3 extension) : ")
sample_name = sample_name + ".mp3"

# Record the sample
try:
    sample1.export(sample_name, format="mp3")
    print("Export Successfull.")

except:
    print("Big fail but I don'ty know why !")

