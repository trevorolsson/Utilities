# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 11:34:53 2022

@author: tzo0018
"""
import glob
from PIL import Image

def main():
    
    ### Path to images (use absolute path)
    path      = path_correct("<path to images>")
    name      = 'name' # Name of resulting gif file
    file_type = "PNG"       # Type of file in folder path
    duration  = 250         # Duration of gif in milliseconds
    loop      = 0           # 0 = loop forever, int > 0 means loop that many times
    convert   = False       # Not working as intended

    return converter(path, name, file_type, duration, loop, convert)

def path_correct(path):
    return path.replace(r'\\' , r'//')

def converter(frame_folder, gif_name, file_type, duration, loop, convert):
    
    def make_gif(frame_folder, gif_name, file_type, duration, loop):
        '''This function takes a folder full of images (ONLY images) and compiles them 
        into a list that saves it into a looping gif. This will make the gif run in
        the order the files are in the folder from top to bottom alphabetically. 
        ie: file1.jpg --> file2.jpg --> file3.jpg --> file4.jpg --> etc.'''
        
        frames    = [Image.open(image) for image in 
                  glob.glob(f"{frame_folder}/*."+"{}".format(file_type))]
        frame_one = frames[0]
        name = "gif_export/{}.gif".format(gif_name)
        frame_one.save( name
                       , format="GIF"
                       , append_images=frames
                       , save_all=True
                       , duration=duration
                       , loop=loop)
        print("The .gif has been generated")
        return name
    
    def to_mp4(gif_name, convert):
        if convert == True:
            import time as t
            cd = 5
            for i in range(cd,0,-1):
                print(f"{i}... ", end="\r", flush=True)
                t.sleep(cd)
            
            import moviepy.editor as mp
            
            mp4 = mp.VideoFileClip(gif_name)
            new_name = gif_name.split('.gif')
            mp4.write_videofile(new_name[0]+'.mp4')
            
            print('\t');print("The .gif has been converted into .mp4")
        else:
            pass
        return
    
    name = make_gif(frame_folder, gif_name, file_type, duration, loop)
    to_mp4(name, convert)
    
    return print('Done!')

if __name__ == "__main__":
    main()
