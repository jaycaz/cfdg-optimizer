# Jordan Cazamias
# CFDG Optimizer
# July 2014

from multiprocessing import Process

import Tkinter
from PIL import ImageFont
from PIL import ImageTk

# Debug text font and color

try:
    font = ImageFont.truetype("")
except IOError as e:
    font = ImageFont.load_default()

color = (0, 255, 0)  # green

runningprocs = {}

def show(image, killothers=False, message=""):
    """
    Show PIL Image, and store child process so image can be closed

    :param image: PIL Image to be shown
    :param killothers: If true, closes all other images
    :param message: Optional message to display above image
    """
    if killothers:
        for img in runningprocs.keys():
            close(img)

    proc = Process(target=_show, args=(image, message))
    proc.start()
    runningprocs[image] = proc
    if not proc.is_alive():
        print "proc is already closed"

def close(image):
    """
    Kills PIL Image show process

    :param image: PIL Image to be closed
    """
    if image in runningprocs:
        imgproc = runningprocs[image]
        if imgproc.is_alive():
            imgproc.terminate()
        runningprocs.pop(image)

def _show(image, message):
    root = Tkinter.Tk()

    # Display Image in Tkinter canvas
    tkimg = ImageTk.PhotoImage(image)
    w = tkimg.width()
    h = tkimg.height()
    canvas = Tkinter.Canvas(root, width=w, height=h)
    canvas.create_image(w/2, h/2, image=tkimg)

    # Add debug information
    if message != "":
        debug = Tkinter.Label(root, text=message, font=("Courier", 14))
        debug.pack()

    canvas.pack()
    Tkinter.mainloop()

