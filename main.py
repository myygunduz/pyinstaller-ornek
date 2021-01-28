import tkinter as tk
from PIL.ImageTk import PhotoImage
from PIL.Image import open

window=tk.Tk()
window.title("Mert Mekatronik")
window.geometry("300x300")

render = PhotoImage(open("logo.png"))
img = tk.Label( image=render)
img.image = render
img.pack()

window.mainloop()
