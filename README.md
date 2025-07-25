# PiP Webcam Viewer

A lightweight always-on-top window for previewing a webcam or other video source.
The window is borderless and can be freely repositioned. It is useful as a small
picture-in-picture monitor and works well with tools like TouchOSC.

## Features

- Opens borderless window in a 320&times;180 window positioned at
  `x=10, y=10`.
- **Right click & drag** to move the window.
- **Middle click** to refresh the video stream.
- Press **0**, **1** or **2** to switch between available cameras.
- **Page&nbsp;Up** and **Page&nbsp;Down** resize to `640x360` or `320x180`.
- Press **L** to enlarge to `960x540`.
- **Escape** or **Alt+F4** closes the viewer.

## Usage

```bash
python PiPViewer.pyw
```

After launching, use the keyboard shortcuts above to change sources or resize the
preview. The window always stays on top of other applications.

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

A version that accepts NDI sources is available on the `PiP NDI` branch. See
<https://github.com/CarlosFdez/pyNDI/tree/master> for the underlying NDI
implementation.

![screenshot](https://github.com/woejefe/MiniWebcamViewer/assets/113958695/a124a9f2-a739-432e-a921-85cd8e269dc9)
