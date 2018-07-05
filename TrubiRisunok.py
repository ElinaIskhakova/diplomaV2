from tkinter import *

root = Tk()

c = Canvas(root, width=900, height=700, bg='white')
c.pack()
c.create_line(50,50,475,50)
c.create_rectangle(250, 50, 275, 250,outline='black', width=3)
c.create_rectangle(256.25, 250, 268.75, 400,outline='black', width=2)
c.create_rectangle(253.125, 400, 271.875, 500,outline='black', width=3)
c.create_rectangle(250, 500, 275, 600,outline='black', width=3)
c.create_polygon(250, 600, 237.5, 625, 262.5, 625)
c.create_polygon(275, 600, 262.5, 625, 287.5, 625)
c.create_line(100, 50, 100, 250,
                width=1, arrow=LAST,
                activefill='lightgreen',
                arrowshape="10 30  10")
root.mainloop()