from pydub.utils import make_chunks
from pydub import AudioSegment

import speech_recognition
import moviepy.editor as editor
import os, glob

# Path of the video file
path = "name_of_video.extension"

clip = editor.VideoFileClip(path).subclip()
clip.audio.write_audiofile("audio.mp3")

audio = AudioSegment.from_file("audio.mp3", "mp3")
size = 180000 # 3 min per chunk

chunks = make_chunks(audio, size)

for i, chunk in enumerate(chunks):
    chunk_name = f'audio{i}.wav'
    chunk.export(chunk_name, format="wav")
    file_audio = speech_recognition.AudioFile("./" + chunk_name)

    recognizer = speech_recognition.Recognizer()
    with file_audio as source:
        audio_text = recognizer.record(source)
        text = recognizer.recognize_google(audio_text, language="pt-BR")

    with open("./text.txt", "a+") as file:
        file.write(text + ' ')

for filename in glob.glob("./audio*"):
    os.remove(filename)
