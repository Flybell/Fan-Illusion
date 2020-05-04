from PIL import Image
import glob
import os


def create_png_folder():
    ## save to png file
    print("checking if png folder exists")
    if not os.path.exists('png/'):
        print("creating a png folder")
        os.mkdir('png/')

    print("removing files from the png folder")
    for file in glob.glob("png/*.png"):
        os.remove(file)

def create_gif():
    frames = []
    imgs = glob.glob("png/*.png")
    for i in imgs:
        new_frame = Image.open(i)
        frames.append(new_frame)

    # Save into a GIF file that loops forever
    print("creating gif file")
    frames[0].save('fan_stimuli.gif', format='GIF',
                   append_images=frames[1:],
                   save_all=True,
                   duration=36, #100 ms = 10 frames per s
                   loop=0)
