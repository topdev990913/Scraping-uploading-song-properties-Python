# import shutil
# shutil.copytree("D:/music_test/2 Live Crew - (Banned)/Banned In The U.S.A", "D:/music_test/2 Live Crew")
# import os
# import shutil

# for root, dirs, files in os.walk('D:/music_test/2 Live Crew - (Banned)'):  # replace the . with your starting directory
#    for file in files:
#       path_file = os.path.join(root,file)
#       shutil.copy2(path_file,'D:/music_test/2 Live Crew')

# importing the modules
import os
import shutil

# Providing the folder path
origin = 'D:/music_test/2 Live Crew - (Banned)'
target = 'D:/music_test/2 Live Crew'

# Fetching the list of all the files
files = os.listdir(origin)

# Fetching all the files to directory
for file_name in files:
   shutil.copy(origin+file_name, target+file_name)
print("Files are copied successfully")
