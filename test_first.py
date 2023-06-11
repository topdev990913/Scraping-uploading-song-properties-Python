import pathlib
import os
import datetime
import pandas as pd
import mutagen
from tinytag import TinyTag
from mutagen.mp3 import MP3
import soundfile as sf
from eyed3 import id3
import audio_metadata
# import stagger
path = "D://music_test"
lists = pathlib.Path(path)
File_Name_list = []
for item in lists.rglob("*"):
    if item.is_file():
        tag = id3.Tag()
        fstat = os.stat(item) 
        if ".jpg" in str(item):
            continue
        Song_path = str(item).replace("\\", "/")
        #####Song Name and extension#####
        name = item.name.capitalize()
        string_split = name.split('.')
        extension = string_split[len(string_split)-1]
        Song_name = name.replace(f".{extension}", "").replace("_", " ") 
        if Song_name in File_Name_list:
            os.remove(Song_path)
        File_Name_list.append(Song_name)
        print(Song_name)
        print(Song_path)
        print(File_Name_list)
