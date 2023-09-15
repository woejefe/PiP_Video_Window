import tkinter as tk
from PIL import Image, ImageTk
from imutils.video import VideoStream
import cv2
import datetime
import finder
import receiver
import lib
import imutils

find = finder.create_ndi_finder()
NDIsources = find.get_sources()
recieveSource = []
print(str(len(NDIsources)) + " NDI Sources Detected")
for x in range(len(NDIsources)):       
        print(str(x) + ". "+NDIsources[x].name + " @ "+str(NDIsources[x].address))  
        receiver.name=receiver.create_receiver(NDIsources[x]) 
        receiver.bandwidth = 100
        
        
        recieveSource.append(receiver.name)
print("Receivers made for all sources found... use number keys to go to corresponding source")        
 #setheight of the window that opens
      
        
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
        self.width  = 320
        self.height = 180  
        self.scale=(self.width,self.height)
        #set the width of the screen inside
        screen_width  = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        #set position of where window and screen opens
        x = 10
        y = 10                
        #format how geometry in injested
        self.window.geometry('{}x{}+{}+{}'.format(self.width, self.height, x, y))
        self.window.geometry('{}x{}'.format(self.width, self.height))
        #window management to close window 
        self.window.wm_protocol("WM_DELETE_WINDOW", self.on_close) 
        #makes the window draggable when Right CLick click is held and moved
        grip=Grip(self.window)
        #Binds Escape Button to close window and middle click to refresh stream
        self.window.bind("<Escape>", self.on_close)  
        # Binds sources to number keys
        self.window.bind("1",self.source1)
        self.window.bind("0",self.source0)
        self.window.bind("2",self.source2)
        self.window.bind("3",self.source3)
        self.window.bind("4",self.source4)
        self.window.bind("5",self.source5)
        self.window.bind("6",self.source6)
        self.window.bind("7",self.source7)
        self.window.bind("8",self.source8)
        self.window.bind("9",self.source9)
        self.window.bind("<w>",self.resizenhd)
        self.window.bind("<q>",self.resizeog)
        self.window.bind("<e>",self.resizeqhd)
        self.window.bind("<r>",self.resizefhd)
        
        #create the capture label for video 
        self.panel = tk.Label(self.window)
        self.panel.pack(side="left")
        #set latency defaults and default source frame to read
        self.stop = False
        self.frame= recieveSource[0]
        self.window.after(33, self.video_loop)
        #starts window in mainloop
        self.window.mainloop()
    def video_loop(self):       
        frame= self.frame.read()
        #reads stream input then converts to correct color range then scales down (using 16:9 ratio)
        image = cv2.cvtColor(frame, cv2.COLOR_BGRA2RGBA)
        resize = cv2.resize(image,self.scale,interpolation=cv2.INTER_LINEAR)
        #sets image for PhotoImage to read input as array
        self.image = Image.fromarray(resize)       
        self.photo = ImageTk.PhotoImage(self.image)  # assigned to class variable `self.photo` so it resolves problem with bug in PhotoImage
        #sets output to panel/label
        self.panel.configure(image=self.photo)
        #Sets how often to get frames from webcam       
        if not self.stop:
            self.window.after(33, self.video_loop)            # 40ms = 25FPS
            #self.window.after(25, self.video_loop)   # 25ms = 40FPS    
    
    def source1(self,e):
        self.frame=recieveSource[1]
    def source0(self,e):
        self.frame=recieveSource[0]
    def source2(self,e):
        self.frame=recieveSource[2]
    def source3(self,e):
        self.frame=recieveSource[3]
    def source4(self,e):
        self.frame=recieveSource[4]
    def source5(self,e):
        self.frame=recieveSource[5]
    def source6(self,e):
        self.frame=recieveSource[6]
    def source7(self,e):
        self.frame=recieveSource[7]
    def source8(self,e):
        self.frame=recieveSource[8]
    def source9(self,e):
        self.frame=recieveSource[9]
    
    def resizefhd(self,e):     
        self.window.geometry('{}x{}'.format(1280 ,720))
        self.scale=(1280, 720)
        print("1280x720")
    
    def resizeqhd(self,e):     
        self.window.geometry('{}x{}'.format(960 ,540))
        self.scale=(960, 540)
        print("qHD")

    def resizenhd(self,e):     
        self.window.geometry('{}x{}'.format(640 ,360))
        self.scale=(640, 360)
        print("nHD")
        
    def resizeog(self,e):     
        self.window.geometry('{}x{}'.format(320 ,180))
        self.scale=(320,180)
        print("320x180")  
    
    
    #def popupmsg(self,e):
       # popup = tk.Tk()
       # popup.wm_title("NDI Sources")
        #label = tk.Label(popup, text=recieveSource)
        #label.pack(side="top", fill="x", pady=10)
     #   B1 = tk.Button(popup, text="Close", command = popup.destroy)
      #  B1.pack()
      #  B2 = tk.Button(popup, text="Source0", command = self.source1())
      #  B2.pack()
        #popup.mainloop()
        
    


    def on_close(self,e):
        self.stop = True
        #self.receiver.stop()
        self.window.destroy()





if __name__ == '__main__':
    MainWindow()
       
