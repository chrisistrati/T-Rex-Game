import pyautogui
import numpy as np
import cv2
import time

big_cactus=cv2.imread("images\big_cactus.png")
small_cactus=cv2.imread("images\small_cacuts.png")

time.sleep(1)
image=np.array(pyautogui.screenshot())
locate_dino=cv2.imread("images\locate dinosaur.png")
result=cv2.matchTemplate(image, locate_dino, cv2.TM_CCOEFF_NORMED)

cv2.imshow("result", result)
cv2.waitKey()
cv2.destroyAllWindows()

time.sleep(2)

min_value, max_value, min_loc, max_loc = cv2. minMaxLoc(result)

w=locate_dino.shape[1]
h=locate_dino.shape[0]
# cv2.rectangle(image, max_loc, (max_loc[0]+w, max_loc[1] + h), (0, 255, 255), 2)

# cv2.imshow("result", image)
# cv2.waitKey()
# cv2.destroyAllWindows()

smol_image=np.array(pyautogui.screenshot(region=(max_loc[0], max_loc[1], w, h)))
# cv2.imshow("wrgt", smol_image)
# cv2.waitKey()
# cv2.destroyAllWindows()

while True:
    smol_image=np.array(pyautogui.screenshot(region=(max_loc[0], max_loc[1], w, h)))
    new_result=cv2.matchTemplate(smol_image, big_cactus, cv2.TM_CCOEFF_NORMED)
    if new_result > 0.8:
        pyautogui.press("up")
