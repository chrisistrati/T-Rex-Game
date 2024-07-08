import pyautogui
import numpy as np
import cv2
import time
import keyboard
from screenshot import grab_screen
from datetime import date

def jump(image, temlpate):
    result=cv2.matchTemplate(image, temlpate, cv2.TM_CCOEFF_NORMED)
    min_value, max_value, min_loc, max_loc = cv2. minMaxLoc(result)
    if max_value>0.6:
        keyboard.press("up arrow")
def duck(image, temlpate):
    result=cv2.matchTemplate(image, temlpate, cv2.TM_CCOEFF_NORMED)
    min_value, max_value, min_loc, max_loc = cv2. minMaxLoc(result)
    if max_value>0.6:
        pyautogui.keyDown("down")
        time.sleep(0.5)
        pyautogui.keyUp("down")
        
def checkObject(image, temlpate):
    answer=False
    result=cv2.matchTemplate(image, temlpate, cv2.TM_CCOEFF_NORMED)
    min_value, max_value, min_loc, max_loc = cv2. minMaxLoc(result)
    if max_value>0.5:
        answer=True
    return answer
def giveMaxLoc(image, temlpate):
    result=cv2.matchTemplate(image, temlpate, cv2.TM_CCOEFF_NORMED)
    min_value, max_value, min_loc, max_loc = cv2. minMaxLoc(result)
    return max_loc

big_cactus=cv2.imread("images/big_cactus.png")
small_cactus=cv2.imread("images\small_cacuts.png")
small_cactus_group=cv2.imread("images\small_cactus_group.png")
pterodactil_up = cv2.imread("images\pterodactil_up.png")
game_over=cv2.imread("images\game_over.png")
pterodactil_down = cv2.imread("images\pterodactil_down.png")

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
cv2.rectangle(image, max_loc, (max_loc[0]+w+650, max_loc[1] + h), (0, 255, 255), 2)

# cv2.imshow("result", image)
# cv2.waitKey()
# cv2.destroyAllWindows()

smol_image=np.array(pyautogui.screenshot(region=(max_loc[0]-int(w/2), max_loc[1]+int(h/2), w, h)))
# edge=np.array(grab_screen(region=(max_loc[0]+500, max_loc[1], w+200, h)))
# cv2.imshow("wrgt", edge)
# cv2.waitKey()
# cv2.destroyAllWindows()


scores=[]
start=time.time()
pyautogui.press(" ")
while True:
    end=time.time()
    duration=end-start
    if duration <=10:
        smol_image=np.array(grab_screen(region=(max_loc[0], max_loc[1], w+90, h)))
    elif duration >10 and duration <=20:
        smol_image=np.array(grab_screen(region=(max_loc[0], max_loc[1], w+120, h)))
    elif duration >20 and duration<=30:
        smol_image=np.array(grab_screen(region=(max_loc[0], max_loc[1], w+140, h)))
    elif duration >30 and duration<=40:
        smol_image=np.array(grab_screen(region=(max_loc[0], max_loc[1], w+160, h)))
    elif duration >40 and duration<=60:
        smol_image=np.array(grab_screen(region=(max_loc[0], max_loc[1], w+200, h)))
    elif duration >60 and duration<=80:
        smol_image=np.array(grab_screen(region=(max_loc[0], max_loc[1], w+220, h)))
    elif duration >80:
        smol_image=np.array(grab_screen(region=(max_loc[0], max_loc[1], w+250, h)))
    

    if duration<=40 and int(duration*10) not in scores:
        scores.append(int(duration*10))
    elif duration>40 and int(duration*11) not in scores:
        scores.append(int(duration*11))
    print(scores[-1]) 
    jump(smol_image, big_cactus)
    jump(smol_image, small_cactus)
    jump(smol_image, pterodactil_down)
    duck(smol_image, pterodactil_up)  
    if keyboard.is_pressed("s"):
        break
    if checkObject(np.array(grab_screen(region=(800, 400, 500, 500))), game_over):
        break
with open("T-Rex Scores.csv", "a") as file:
    file.write(f"\n{max(scores)},{date.today()}")
    

    
