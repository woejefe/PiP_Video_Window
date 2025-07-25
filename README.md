# PiP Webcam Viewer

A lightweight always-on-top window for previewing a webcam or other video source.
The window is borderless and can be freely repositioned. It is useful as a small
picture-in-picture monitor and works well with tools like TouchOSC.

## Features

- Opens borderless window in a 320&times;180 window positioned at
  `x=10, y=10`.
- **Right click & drag** to move the window.
- **Escape** or **Alt+F4** closes the viewer.
- **F1** for source menu **F2** for help menu

## Usage

```bash
python PiPViewer.py
```

After launching, use the buttons to change sources in the main window. if you need to re-select a source use **F1** to pull up source menu
The window always stays on top of other applications.
Use refresh key in Source menu to update sources
Use RTSP key to add a network stream

## Dependencies

- Python 3
- Pillow
- imutils
- OpenCV (`cv2`)
- tkinter (usually included with standard Python installs)

Install them with pip:

```bash
pip install pillow imutils opencv-python
```

## Additional Notes
See <https://github.com/CarlosFdez/pyNDI/tree/master> for the underlying NDI
implementation.

![screenshot](https://github.com/woejefe/MiniWebcamViewer/assets/113958695/a124a9f2-a739-432e-a921-85cd8e269dc9)
