import cv2
import os
import time
os.chdir(os.path.dirname(os.path.abspath(__file__)))

PLAYING = False

def get_terminal_width():
    try:
        return os.get_terminal_size().columns
    except OSError:
        return 80

def frame_to_ascii(frame, width):
    ASCII_CHARS = " .,-+=:;!?08#"
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    h, w = gray.shape
    if w < 2 or h < 2:
        return "[!] Resolution"
    aspect_ratio = h / w
    new_height = max(1, int(aspect_ratio * width * 0.55))
    resized = cv2.resize(gray, (width, new_height))
    return "\n".join(
        "".join(ASCII_CHARS[pixel * len(ASCII_CHARS) // 256]
 for pixel in row)
        for row in resized
    )

def frame_to_ascii_color(frame, width):
    ASCII_CHARS = "#"
    height, orig_width, _ = frame.shape
    aspect_ratio = height / orig_width
    new_height = max(1, int(aspect_ratio * width * 0.55))
    resized = cv2.resize(frame, (width, new_height))

    lines = []
    for row in resized:
        line = []
        for pixel in row:
            b, g, r = pixel
            intensity = int(0.299*r + 0.587*g + 0.114*b)
            char = ASCII_CHARS[intensity * len(ASCII_CHARS) // 256]
            line.append(f"\033[38;2;{r};{g};{b}m{char}\033[0m")
        lines.append("".join(line))
    return "\n".join(lines)



def play_video_ascii(path, mode):
    cap = cv2.VideoCapture(path)
    if not cap.isOpened():
        print("[!] Can't open: " + path)
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    if not fps or fps <= 1:
        fps = 30
    delay = 1 / fps

    width = get_terminal_width()

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if (mode == "0"):
            ascii_frame = frame_to_ascii(frame, width)
        elif (mode == "1"):
            ascii_frame = frame_to_ascii_color(frame, width)
        print("\033[H" + ascii_frame, end="", flush=True)
        time.sleep(delay)

    cap.release()


while True:
    try:
        ip = input("name : ").split(" ")
        if (ip[0] == "clear"):
            print("\033[2J\033[H", end="", flush=True)
            continue
        if (ip[0] == "exit"):
            break
        if len(ip) < 2:
            print("Path or mode excepted, Syntax: <path> <mode[0 (grayscale), 1 (color)]>")
            continue
        PLAYING = True
        play_video_ascii(ip[0], ip[1])
    except KeyboardInterrupt:
        if not PLAYING:
            break
        print("Stopped")
        PLAYING = False
    except EOFError:
        break
