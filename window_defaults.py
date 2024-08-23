# window_defaults.py

import win32gui

def set_window_position(window_title, x, y, width, height):
    hwnd = win32gui.FindWindow(None, window_title)
    if hwnd:
        win32gui.MoveWindow(hwnd, x, y, width, height, True)

def get_window_position(window_title):
    hwnd = win32gui.FindWindow(None, window_title)
    if hwnd:
        rect = win32gui.GetWindowRect(hwnd)
        x, y, right, bottom = rect
        width = right - x
        height = bottom - y
        return x, y, width, height
    return None, None, None, None
