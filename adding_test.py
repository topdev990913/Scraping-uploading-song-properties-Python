from tinytag import TinyTag
from eyed3 import id3
tag = id3.Tag()
tag.parse("Get Ready For This.mp3")
Song_artist = str(tag.artist)
print(Song_artist)