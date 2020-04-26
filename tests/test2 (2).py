from tkinter import *
root = Tk()
image = PhotoImage(file='insert_path_picture.gif')
canvas = Canvas(root, width=1, height=1)
canvas.pack(fill=BOTH, expand=1)
canvas.create_image(0, 0, image=image, anchor=NW)
canvas.create_text(0, 20, text='Woohoo!', anchor=W)
root.geometry('80x80')
root.mainloop()
