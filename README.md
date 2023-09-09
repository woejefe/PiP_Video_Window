# PiP WebcamViewer / Pip-Window (used for NDI/OBS webcam viewer)

I wanted a way to display a video input such as; NDI,RTMP,Webcam,CaptureDevice, for a preview window viewer in a borderless window without it affecting other windows that always stays on top.

  --Opens first webcam input on main screen in 360x180 window... Alt+F4 to exit... it always stays on top
  
  --Works great with TouchOSC to preview a window if using for video mixer . Just drag into position

You can use it as a monitor to see whats happening in on other devices/streams/ basically whatever you can pipe into a webcam input


Currently need help on line 74 (should be easy just need to make a variable for the line "self.stream=VideoStream(0)") and also want to have a way to retry the connection on failed frame or display that the connection is in use elsewhere (after x failed frames)

Dependencies are pillow, imutils, tkinter, and C2V 













https://github.com/woejefe/MiniWebcamViewer/assets/113958695/a124a9f2-a739-432e-a921-85cd8e269dc9

