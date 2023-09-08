from tkinter import *

class Grip:
    ''' Makes a window dragable. '''
    def __init__ (self, parent, disable=None, releasecmd=None) :
        self.parent = parent
        self.root = parent.winfo_toplevel()

        self.disable = disable
        if type(disable) == 'str':
            self.disable = disable.lower()

        self.releaseCMD = releasecmd

        self.parent.bind('<Button-1>', self.relative_position)
        self.parent.bind('<ButtonRelease-1>', self.drag_unbind)

    def relative_position (self, event) :
        cx, cy = self.parent.winfo_pointerxy()
        geo = self.root.geometry().split("+")
        self.oriX, self.oriY = int(geo[1]), int(geo[2])
        self.relX = cx - self.oriX
        self.relY = cy - self.oriY

        self.parent.bind('<Motion>', self.drag_wid)

    def drag_wid (self, event) :
        cx, cy = self.parent.winfo_pointerxy()
        d = self.disable
        x = cx - self.relX
        y = cy - self.relY
        if d == 'x' :
            x = self.oriX
        elif d == 'y' :
            y = self.oriY
        self.root.geometry('+%i+%i' % (x, y))

    def drag_unbind (self, event) :
        self.parent.unbind('<Motion>')
        if self.releaseCMD != None :
            self.releaseCMD()



def main():
    root = Tk()
    root.geometry("200x200")
    root.resizable(0, 0)
    root.overrideredirect(1)
    ot_but=root.attributes('-topmost', 'true')

    back = Frame(root, bg="grey")
    back.pack_propagate(0)
    back.pack(fill=BOTH, expand=1)

    top_Frame = Frame(back, bg="#505050")
    top_Frame.place(x=0, y=0, anchor="nw", width=200, height=5)
    
    grip = Grip(top_Frame)

    Ext_but = Button(top_Frame, text="X", bg="#FF6666", fg="white", command=lambda: exit())
    Ext_but.place(x=170, y=0, anchor="nw", width=30, height=5)
    
    ontop_but = Button(top_Frame, text="OT", bg="blue", fg="white", command=lambda: ot_but)
    ontop_but.place(x=110, y=0, anchor="nw", width=40, height=5)

    root.mainloop()

main()