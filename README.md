# ASCII-Of-Video

A simple but effective Python script that takes video playback on the terminal to the next level.
**Converts videos to ASCII characters** and plays them directly in the terminal.

---

## Features

- <img src="https://api.iconify.design/lucide:play.svg?color=blue" /> Playing video by converting it to ASCII characters
- <img src="https://api.iconify.design/lucide:palette.svg?color=orange" /> Color (ANSI) and black-and-white mode support
- <img src="https://api.iconify.design/lucide:zap.svg?color=yellow" /> Synchronized playback by FPS
- <img src="https://api.iconify.design/lucide:monitor.svg?color=cyan" /> Automatic adaptation to terminal width
- <img src="https://api.iconify.design/lucide:keyboard.svg?color=green" /> Simple command system (interactive use)

---

## Example

![ASCII-Of-Video Demo](example.gif)

---

## Requirements

Only ONE external library:

```bash
pip install opencv-python
```

Python built-in modules:

- `os`
- `time`

---

## Use

Run the script:

```bash
python main.py
```

Then provide the video path and mode:

```bash
<video_path> <mode>
```

### Example:

```bash
video.mp4 0
video.mp4 1
```

---

## Modes

| Mode | Description        |
| ---- | ------------------ |
| `0`  | B&W ASCII          |
| `1`  | Color ASCII (ANSI) |

---

## How Does It Work? (Technical Details)

(1) Video is read frame by frame (`cv2.VideoCapture`)
(2) Each frame:

- rendered in grayscale or color
- Mapped to ASCII characters
  (3) Printed to the terminal (overwrite with `\033[H`)
  (4) Delay is applied according to FPS

---

## ⚠️ Known Limitations

- Terminal performance can be limiting
- Color mode is slower
- Very high resolution output may be distorted
- Modern terminal is recommended over Windows CMD (Windows Terminal, iTerm, etc.)

---

## Commands

```bash
clear   -> clears the screen
exit    -> exits the program
```

---

## Development Ideas

- [ ] Frame skip / adaptive FPS
- [ ] Audio support (separate thread)
- [ ] More advanced ASCII mapping (gradient character sets)
- [ ] GPU acceleration (OpenCV CUDA)
- [ ] CLI argument support (argparse)
- Honestly, the possibilities are endless for a fun project like this!

---

## Small Note

In color mode, only one character (`#`) is used.
For more detailed images, the ASCII set can be extended, but it may impact performance.:

```python
ASCII_CHARS = " .:-=+*#%@"
```

---

## License

Actually, Do What The F\*ck You Want To Public License (WTFPL)

---

![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/EnbloxC3/ASCII-Of-Video)