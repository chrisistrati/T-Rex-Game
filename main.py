import pyautogui
import numpy as np
import cv2
import time
import keyboard

def move(image, temlpate, direction):
    result=cv2.matchTemplate(image, temlpate, cv2.TM_CCOEFF_NORMED)
    min_value, max_value, min_loc, max_loc = cv2. minMaxLoc(result)
    if max_value>0.6:
        pyautogui.press(direction)
def checkObject(image, temlpate):
    answer=False
    result=cv2.matchTemplate(image, temlpate, cv2.TM_CCOEFF_NORMED)
    min_value, max_value, min_loc, max_loc = cv2. minMaxLoc(result)
    if max_value>0.6:
        answer=True
    return answer

big_cactus=cv2.imread("images/big_cactus.png")
small_cactus=cv2.imread("images\small_cacuts.png")
small_cactus_group=cv2.imread("images\small_cactus_group.png")
pterodactil_up = cv2.imread("images\pterodactil_up.png")

# time.sleep(1)
image=np.array(pyautogui.screenshot())
dino=cv2.imread("images\dinosaur.png")
result=cv2.matchTemplate(image, dino, cv2.TM_CCOEFF_NORMED)

# cv2.imshow("result", result)
# cv2.waitKey()
# cv2.destroyAllWindows()

# time.sleep(2)

min_value, max_value, min_loc, max_loc = cv2. minMaxLoc(result)

w=dino.shape[1]
h=dino.shape[0]
cv2.rectangle(image, max_loc, (max_loc[0]+w, max_loc[1] + h), (0, 255, 255), 2)

# cv2.imshow("result", image)
# cv2.waitKey()
# cv2.destroyAllWindows()

smol_image=np.array(pyautogui.screenshot(region=(max_loc[0]-int(w/2), max_loc[1]+int(h/2), w, h)))
# cv2.imshow("wrgt", smol_image)
# cv2.waitKey()
# cv2.destroyAllWindows()
start=time.time()
while True:
    end=time.time()
    duration=end-start
    if duration <=18:
        smol_image=np.array(pyautogui.screenshot(region=(max_loc[0], max_loc[1], w+140, h)))
    elif duration >18 and duration <=24:
        smol_image=np.array(pyautogui.screenshot(region=(max_loc[0], max_loc[1], w+200, h)))
    elif duration >24 and duration<=32:
        smol_image=np.array(pyautogui.screenshot(region=(max_loc[0], max_loc[1], w+230, h)))
    elif duration >32:
        smol_image=np.array(pyautogui.screenshot(region=(max_loc[0], max_loc[1], w+250, h)))
    print(duration)
    move(smol_image, big_cactus, "up")
    move(smol_image, small_cactus, "up")
    move(smol_image, pterodactil_up, "down")  
    if keyboard.is_pressed("s"):
        break
        
    

    
#last line