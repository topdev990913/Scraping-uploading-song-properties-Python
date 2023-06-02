import subprocess
import os
from pathlib import Path
import glob
import pandas as pd
from datetime import datetime
from eyed3 import id3
from mutagen.mp3 import MP3
import pathlib
tag = id3.Tag()
# path = "//NAS-1/Music"
path = "D://music"
lists = pathlib.Path(path)
# start = Path(path)
# lists = list(start.rglob("*mp3"))

st_size_list = []
file_name_list = []
new_data = {}
result_list = []
name_list = []
file_path_list = []
artist_list = []
album_list = []
path_list = []
length_list = []
genre_list = []
publisher_list = []
bitrate_list = []
extension_list = []
# for item in lists:
for item in lists.rglob("*"):
    if item.is_file():
        print(item)
        fstat = os.stat(item) 
        #######Song Name########
        st_name_a = item.name
        st_name_b = st_name_a.capitalize()
        st_name_c = st_name_b.replace("amp;", "").replace("&", "").replace("the origin", "") 
        st_name_d = st_name_c.replace(".mp3", "").replace(".wma", "")
        st_name = st_name_d.strip()
        if st_name in file_name_list:
                continue
        file_name_list.append(st_name)        
        new_data['name'] = st_name

        #######Song Size#######  
        st_size_a = fstat.st_size
        st_size_b = float(st_size_a)/1024/1024
        st_size = str(st_size_b)
        st_size_list.append(st_size)
        new_data['st_size'] = st_size 


        a = str(item).replace("\\", "//")
        tag.parse(a)

        ######Song Artist######
        artist = str(tag.artist).replace(" - (Banned)", "")
        artist_list.append(artist)
        new_data['artist'] = artist

        ######Song Album########
        album = tag.album
        album_list.append(album)  
        new_data['album'] = album 

        ######Song Genre#######
        genre_first = str(tag.genre).replace("(", "").replace(")", "")
        genre = ''.join([i for i in genre_first if not i.isdigit()])
        genre_list.append(genre)
        new_data['Genre'] = genre

        ######Song Publisher###
        publisher = tag.publisher
        publisher_list.append(publisher)
        new_data['publisher'] = publisher

        # audio = MP3(a)
        # length_first = audio.info.length
        # length = round(length_first, 0)
        # bitrate = audio.info.bitrate / 1000


        ######Song_path#########
        file_path = str(item).replace(" - (Banned)", "")              
        file_path_list.append(file_path)
        new_data['file_path'] = file_path

        ######Song Type#########
        d = st_name_b.split('.')
        extension = d[len(d)-1]
        extension_list.append(extension)
        new_data['File Type'] = extension
        
        # bitrate_list.append(bitrate)
        # new_data['bitrate'] = bitrate

        
        
        

        

        

        

        # length_list.append(length)
        # new_data['length'] = length
        
               
        
        result_list.append(new_data)

        # dict = {'name': file_name_list, 'File_path': file_path_list, 'Item Type': extension_list,  'File_size_in_MB': st_size_list, 'Length': length_list, 'Artist': artist_list, 'Album': album_list, 'Genre': genre_list, 'publisher': publisher_list, 'bitrate': bitrate_list}
        dict = {'name': file_name_list, 'File_path': file_path_list, 'Item Type': extension_list,  'File_size_in_MB': st_size_list, 'Artist': artist_list, 'Album': album_list, 'Genre': genre_list, 'publisher': publisher_list}
        df = pd.DataFrame(dict)

        df.to_csv('Result_music_list.csv')

print(result_list)
