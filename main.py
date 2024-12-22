import pygetwindow as gw
import win32gui
import win32api
import win32con
from math import sqrt
import time

CURRENT_SCREEN_SIZE = 27        # in inches
CURRENT_SCREEN_WIDTH = 2560     # in pixels
CURRENT_SCREEN_HEIGHT = 1440    # in pixels

CHU3_SCREEN_SIZE = 32           # you likely won't need to change that
CHU3_SCREEN_WIDTH = 1920        # same
CHU3_SCREEN_HEIGHT = 1080       # same


def calculate_factor():
    diag_res_1 = sqrt(CURRENT_SCREEN_WIDTH ** 2 + CURRENT_SCREEN_HEIGHT ** 2)
    dpi_1 = diag_res_1 / CURRENT_SCREEN_SIZE
    diag_res_2 = sqrt(CHU3_SCREEN_WIDTH ** 2 + CHU3_SCREEN_HEIGHT ** 2)
    dpi_2 = diag_res_2 / CHU3_SCREEN_SIZE

    return dpi_1 / dpi_2

def calculate_pixels_to_crop():
    return int(CURRENT_SCREEN_HEIGHT - CHU3_SCREEN_HEIGHT * CHU3_SCREEN_SIZE / CURRENT_SCREEN_SIZE)

def set_window_size_and_position(hwnd, width, height, x, y):
    win32gui.MoveWindow(hwnd, x, y, width, height, True)

def align_window_bottom(window_title, zoom_factor):
    try:
        window = next(w for w in gw.getAllTitles() if window_title in w)
    except StopIteration:
        print(f"Window with title containing '{window_title}' not found.")
        return None

    hwnd = gw.getWindowsWithTitle(window)[0]._hWnd

    screen_width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    screen_height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)

    rect = win32gui.GetWindowRect(hwnd)
    original_width = rect[2] - rect[0]
    original_height = rect[3] - rect[1]
    original_x = rect[0]
    original_y = rect[1]

    zoomed_width = int(original_width * zoom_factor)
    zoomed_height = int(original_height * zoom_factor)

    new_x = (screen_width - zoomed_width) // 2  # Center horizontally
    new_y = screen_height - zoomed_height       # Align bottom

    set_window_size_and_position(hwnd, zoomed_width, zoomed_height, new_x, new_y)

    return hwnd, original_width, original_height, original_x, original_y

def restore_window(hwnd, width, height, x, y):
    set_window_size_and_position(hwnd, width, height, x, y)

try:
    window_title = "teaGfx DirectX Release"
    zoom_factor = calculate_factor()
    print(f"Scaling factor: {zoom_factor}")
    print(f"{calculate_pixels_to_crop()} pixels cropped from the top.")

    result = align_window_bottom(window_title, zoom_factor)
    if result is None:
        exit()

    hwnd, orig_width, orig_height, orig_x, orig_y = result

    print("Press Ctrl+C to stop and reset the window.")
    while True:
        time.sleep(1)

finally:
    try:
        restore_window(hwnd, orig_width, orig_height, orig_x, orig_y)
        print("Window restored to its original size and position.")
    except Exception as e:
        print(f"Failed to restore window: {e}")