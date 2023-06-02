import subprocess
import os
from pathlib import Path
import glob
import pandas as pd
import datetime
from eyed3 import id3
import eyed3
from mutagen.mp3 import MP3
import mutagen
import pathlib
tag = id3.Tag()
path = "D://music"
start = Path(path)
lists = list(start.rglob("*mp3"))

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
Rate_list = []
comments_list = []
st_mtime_list = []
st_ctime_list = []
for item in lists:
        fstat = os.stat(item) 
        aa = str(item).replace("\\", "//")
        tag.parse(aa)
        ######Song Name########
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

        ######Song Modified time#######
        mtime = os.path.getmtime(aa)
        st_mtime = datetime.datetime.fromtimestamp(mtime)
        st_mtime_list.append(st_mtime)
        new_data['st_mtime'] = st_mtime
        
        ######Song Created time######
        ctime = os.path.getctime(aa)
        st_ctime = datetime.datetime.fromtimestamp(ctime)
        st_ctime_list.append(st_ctime)
        new_data['st_ctime'] = st_ctime


        

        ######Song artist######
        artist = str(tag.artist).replace(" - (Banned)", "")
        artist_list.append(artist)
        new_data['artist'] = artist

        ######Song album########
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
        
        ######Song Length######
        audio = MP3(aa)
        length_first = audio.info.length
        length = round(length_first, 0)
        length_list.append(length)
        new_data['length'] = length

        ######Song Bitrate#####
        bitrate = audio.info.bitrate / 1000
        bitrate_list.append(bitrate)
        new_data['bitrate'] = bitrate

        ######Song_path#########
        file_path = str(item).replace(" - (Banned)", "")              
        file_path_list.append(file_path)
        new_data['file_path'] = file_path

        ######Song Type#########
        d = st_name_b.split('.')
        extension = d[len(d)-1]
        extension_list.append(extension)
        new_data['File Type'] = extension

        #####Song Rate########
        audio_info = mutagen.File(aa).info
        Rate = audio_info.sample_rate 
        Rate_list.append(Rate)
        new_data['Rating'] = Rate

        #####Song Comments#######
        audio_comment = eyed3.load(aa)
        try:
                Comments = audio_comment.tag.comments[0].text
        except:
                Comments = "none"
        comments_list.append(Comments)
        new_data['Comments'] = Comments

        result_list.append(new_data)
        

        dict = {'name': file_name_list, 'File_path': file_path_list, 'Item Type': extension_list,  'File_size_in_MB': st_size_list, 'Length': length_list, 'artist': artist_list, 'album': album_list, 'Genre': genre_list, 'publisher': publisher_list, 'bitrate': bitrate_list,'Rating': Rate_list, 'Comments': comments_list, 'Created time': st_ctime_list, 'Modified time': st_mtime_list}
        df = pd.DataFrame(dict)

        df.to_csv('Result_music_list.csv')

print(result_list)
