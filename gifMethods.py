#!/user/bin/env python3

"""
Creates a gif file in a gifs folder
By stitching together png files in a png folder
"""

from PIL import Image
import glob
import os


def create_png_folder():
    if not os.path.exists('png/'):
        os.mkdir('png/')
    for file in glob.glob("png/*.png"):
        os.remove(file)

def create_gif(filename):
    frames = []
    imgs = glob.glob("png/*.png") #save frames to png folder
    for i in imgs:
        new_frame = Image.open(i)
        frames.append(new_frame)

    gif_file = "gifs/" + filename #save gif to gif folder

    # Save into a GIF file that loops forever
    frames[0].save(gif_file, format='GIF',
                   append_images=frames[1:],
                   save_all=True,
                   duration=36, #100 ms = 10 frames per s
                   loop=0)
