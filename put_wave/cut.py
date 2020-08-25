# https://linuxize.com/post/how-to-install-ffmpeg-on-ubuntu-18-04/

# на сервак надо накатить ffmpeg

from pydub import AudioSegment
# from pydub.utils import which

# AudioSegment.converter = which("ffmpeg")
sound = AudioSegment.from_file("/var/www/scripts/put_wave/11111.wav", format="mp3")


duration = len(sound)   

extract = sound[:8500]
print(duration)
extract.export('11111111-extract.mp3', format="mp3")