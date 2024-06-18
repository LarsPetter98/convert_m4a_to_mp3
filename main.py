#You also need to have ffmpeg installed in order for this script to work
from pydub import AudioSegment

def convert_m4a_to_mp3(m4a_file, mp3_file_path):
    audio = AudioSegment.from_file(m4a_file, format="m4a")
    audio.export(mp3_file_path, format="mp3")
    
if __name__ == "__main__":
    m4a_file_path = "./song.m4a"
    mp3_file_path = "./song.mp3"
    convert_m4a_to_mp3(m4a_file_path, mp3_file_path)