#script to convert mkv files to mp4. You need to run the script in the same folder where you have your mkv files

import glob
import os

class convert_mkv_to_mp4:
    
    def __init__(self):

        self.list_of_files = glob.glob("*")
    
    def convert_files(self):

        for j in self.list_of_files:
            j = "'"+j+"'" #Adding this so that we dont have to deal with escape sequences 
            os.system('ffmpeg -i {} -codec copy {}'.format(j,j[:-4]+".mp4'"))

convert = convert_mkv_to_mp4().convert_files()
