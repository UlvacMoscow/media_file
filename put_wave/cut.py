# https://linuxize.com/post/how-to-install-ffmpeg-on-ubuntu-18-04/

# на машину надо накатить ffmpeg

from pydub import AudioSegment

sound = AudioSegment.from_file("/var/www/scripts/put_wave/source.wav", format="mp3")


duration = len(sound)   

extract = sound[:8500]
print(duration)
extract.export('source-extract.mp3', format="mp3")