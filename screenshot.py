import win32gui
import win32ui
import win32con
import win32com.client
from ctypes import windll
from PIL import Image
import ctypes


def screen_monster_td():
    hwnd_target = win32gui.FindWindow(None, 'IdleMonsterTD')

    left, top, right, bot = win32gui.GetWindowRect(hwnd_target)
    w = right - left
    h = bot - top
    
    # Trick so setForeground always works
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(hwnd_target)

    hdesktop = win32gui.GetDesktopWindow()
    hwndDC = win32gui.GetWindowDC(hdesktop)
    mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()

    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)

    saveDC.SelectObject(saveBitMap)

    result = saveDC.BitBlt((0, 0), (w, h), mfcDC, (left, top), win32con.SRCCOPY)

    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)

    im = Image.frombuffer(
        'RGB',
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        bmpstr, 'raw', 'BGRX', 0, 1)

    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hdesktop, hwndDC)

    if result == None:
        # PrintWindow Succeeded
        return im, (left, top, right, bot)
        # im.save("screenshot.png")
    
    return None


# screen_monster_td()