import tkinter as tk
from PIL import Image, ImageTk
from imutils.video import VideoStream
import cv2
import datetime


class Grip:
    ''' Makes a window dragable. '''
    def __init__ (self, parent, disable=None, releasecmd=None) :
        self.parent = parent
        self.root = parent.winfo_toplevel()
        self.disable = disable
        if type(disable) == 'str':
            self.disable = disable.lower()
        self.releaseCMD = releasecmd
        self.parent.bind('<Button-3>', self.relative_position)
        self.parent.bind('<ButtonRelease-3>', self.drag_unbind)
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
            

            
class MainWindow:
    def __init__(self):    
        self.window = tk.Tk()
        #set background and title
        self.window.title("WebcamViewer")
        self.window['bg'] = 'black'
        #set window to be op top of all windows and borderless
        self.window.overrideredirect(1)
        self.window.attributes('-topmost', 'true')
        #setheight of the window that opens
        width  = 320
        height = 180      
        #set the width of the screen inside
        screen_width  = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        #set position of where window and screen opens
        x = 10
        y = 10
        #select source
        source=0                    
        #format how geometry in injested
        self.window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.window.geometry('{}x{}'.format(width, height))
        #no clue honestly... was copied... create the capture label for video maybe???
        self.panel = tk.Label(self.window)
        self.panel.pack(side="left")
        #open webcam.... 'source' corresponds to the webcam input,,, looking to make a dropdown on middle click to select source
        self.stream = VideoStream(source)
        self.stream.start()
        #set latency defaults
        self.stop = False
        self.window.after(30, self.video_loop)
        #window management to close window 
        self.window.wm_protocol("WM_DELETE_WINDOW", self.on_close) 
        #makes the window draggable when Right CLick click is held and moved
        grip = Grip(self.window)
        #Binds Escape Button to close window and double right click to refresh stream
        self.window.bind("<Escape>", exit)              
        #closes loop
        self.window.mainloop()
    # function to get frames from webcam input
    def video_loop(self):      
        width  = 320
        height = 180
        scale = (width, height)
        frame = self.stream.read()
        #reads stream input then converts to correct color range then scales down (using 16:9 ratio)
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        resize = cv2.resize(image,scale,interpolation=cv2.INTER_LINEAR)
        #sets image for PhotoImage to read input as array
        self.image = Image.fromarray(resize)       
        self.photo = ImageTk.PhotoImage(self.image)  # assigned to class variable `self.photo` so it resolves problem with bug in PhotoImage
        #sets output to panel/label
        self.panel.configure(image=self.photo)
        #Sets how often to get frames from webcam       
        if not self.stop:
            self.window.after(30, self.video_loop)            # 40ms = 25FPS
            #self.window.after(25, self.video_loop)   # 25ms = 40FPS   
    #calls function to exit on escape button   
    def popup(e):
        self.window.popup.tk_popup(10,10,0)
    
    def exit(e):
        self.window.destroy()
   #closes out all loops                       
    def on_close(self):
        self.stop = True
        self.stream.stop()
        self.window.destroy()       
 
 #calls on the main loop   
if __name__ == '__main__':
    MainWindow()
