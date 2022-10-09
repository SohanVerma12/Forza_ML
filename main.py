from mss import mss # pip install mss # https://python-mss.readthedocs.io/    for Python
import cv2   # pip install opencv-python # https://pypi.org/project/opencv-python/ for Python

game_area = {"left": -30, "top": 0, "width": 100, "height": 100}    # Game area

def collect_frames():
    gamecap = mss.grab(game_area)

if __name__ == "__main__":
    pass    # Main