import cv2 as cv2
import numpy as np
import time
import screenshot 
import pyautogui
from matplotlib import pyplot as plt

def get_xy_center(coords, max_loc, template):
    left, top, _, _ = coords
    w, h = template.shape[::-1]
    return left + max_loc[0] + w/2, top + max_loc[1] + h/2

def get_monster_td_screenshot():
    pil_img, coords = screenshot.screen_monster_td()
    img = cv2.cvtColor(np.asarray(pil_img), cv2.COLOR_RGB2GRAY)
    return img, coords

def match_image(img, template):
    matching_method = cv2.TM_CCOEFF_NORMED
    # Apply template Matching
    res = cv2.matchTemplate(img, template, matching_method, mask=None)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print(max_val)
    return max_val, max_loc


def showImage(img, max_loc):

    def getCoords(template, max_loc):
        w, h = template.shape[::-1]
        bottom_right = (max_loc[0] + w, max_loc[1] + h)
        return bottom_right

    bottom_right = getCoords(img, max_loc)
    cv2.rectangle(img, max_loc, bottom_right, 255, 5)
    # plt.subplot(121),plt.imshow(res,cmap = 'gray')
    # plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img, cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle('cv2.TM_CCOEFF_NORMED')
    plt.show()

def click(x, y):
    # pyautogui.moveTo(x, y)
    pyautogui.click(x, y)


def searchTemplate(img, coords, template):
    max_val, max_loc = match_image(img, template)

    # We will consider that the template was found if the confidence is bigger than 87%
    if (max_val > 0.87):     
        # Get the coordinates of the center of the image 
        x, y = get_xy_center(coords, max_loc, template)
        # Click it
        click(x, y)
        return True
    else:
        return False


def main():
    play_button = cv2.imread('./templates/PlayButton.jpg', 0)
    cargo_ready = cv2.imread('./templates/CargoReady.jpg', 0)
    dron_ready  = cv2.imread('./templates/DronReady.jpg', 0)

    while(True):
        try:
            img, coords = get_monster_td_screenshot()

            # Dron
            found = searchTemplate(img, coords, dron_ready)
            if (found):
                time.sleep(0.2)
                img, coords = get_monster_td_screenshot()
                searchTemplate(img, coords, play_button)

            # Cargo
            img, coords = get_monster_td_screenshot()
            time.sleep(0.1)
            found = searchTemplate(img, coords, cargo_ready)
            if (found):
                time.sleep(0.2)
                img, coords = get_monster_td_screenshot()
                searchTemplate(img, coords, play_button)
                
        except Exception as e:
            print(e) 
        time.sleep(15)

main()