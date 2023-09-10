# PiP Webcam Viewer / Pip Window / Borderless Window

I wanted a way to display a video input such as; NDI,RTMP,Webcam,CaptureDevice, for a preview window viewer in a borderless window without it affecting other windows that always stays on top.

  --Opens first webcam input on main screen in 360x180 at x=10,y=10 in draggable window... Alt+F4 or Escape Button to exit... it always stays on top.
  
  --Drag with Right Click

  --Refresh video_loop with middle click
  
  --Works great with TouchOSC to preview a window if using for video mixer . Just drag into position

You can use it as a monitor to see whats happening in on other devices/streams/ basically whatever you can pipe into a webcam input


Currently need help on line 74 (should be easy just need to make a variable for the line "self.stream=VideoStream(0)") and also want to have a way to retry the connection on failing to get device 

Dependencies are pillow, imutils, tkinter, and C2V 



Thanks to https://github.com/CarlosFdez/pyNDI/tree/master i made a version that takes in NDI sources into the same type of window













https://github.com/woejefe/MiniWebcamViewer/assets/113958695/a124a9f2-a739-432e-a921-85cd8e269dc9

