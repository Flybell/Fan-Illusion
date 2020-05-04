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
    imgs = glob.glob("png/*.png")
    for i in imgs:
        new_frame = Image.open(i)
        frames.append(new_frame)

    # Save into a GIF file that loops forever
    frames[0].save(filename, format='GIF',
                   append_images=frames[1:],
                   save_all=True,
                   duration=36, #100 ms = 10 frames per s
                   loop=0)
