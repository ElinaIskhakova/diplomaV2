from tkinter import *

root = Tk()

c = Canvas(root, width=900, height=700, bg='white')
c.pack()
c.create_line(50,50,475,50)
c.create_rectangle(245, 50, 280, 250,outline='black', width=2)
c.create_rectangle(256.25, 250, 268.75, 400,outline='black', width=2)
c.create_rectangle(253.125, 400, 271.875, 500,outline='black', width=2)
c.create_rectangle(245, 500, 280, 600,outline='black', width=2)
c.create_polygon(245, 600, 227.5, 615, 262.5, 615)
c.create_polygon(280, 600, 262.5, 615, 297.5, 615)
c.create_line(100, 50, 100, 250,
                width=1, arrow=LAST,
                activefill='lightgreen',
                arrowshape="10 30  10")
root.mainloop()