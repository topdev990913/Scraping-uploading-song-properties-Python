# # from tinytag
# import eyed3

# audio_file = eyed3.load("Get Ready For This.mp3") # Load audio file
# artist = audio_file.tag.albumartist
# audio_file.tag.albumartist = "New Artist" # Set new title
# audio_file.tag.save()
# artist1 = audio_file.tag.albumartist
# print(artist)
# print(artist1)
from mutagen.easyid3 import EasyID3

# Load audio file
audio_file = EasyID3("Get Ready For This.mp3")

# Get current comment
comment = audio_file['comment']
print(comment)
# Update comment
audio_file['comment'] = "New comment"

# Save changes to the file
audio_file.save()
print(audio_file['comment'])

