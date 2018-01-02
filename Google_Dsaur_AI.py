from pynput import keyboard
from PIL import ImageGrab
import numpy as np
import cv2

controller = keyboard.Controller()

def manipulate(original_image):
      processed_img = cv2.cvtColor(np.array(original_image), cv2.COLOR_BGR2RGB)
      processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
      return processed_img


def jump():
    controller.press(keyboard.Key.space)
    #controller.release(keyboard.Key.space)

#last = time.time()
while True:
    screen  = ImageGrab.grab(bbox=(132,196,152,230 ))
    #printscreen_numpy = np.array(printscreen_pil.getdata(), dtype='uint8').reshape((printscreen_pil.size[1], printscreen_pil.size[0],3))
    #print(time.time()-last)
    #last= time.time()
    new_screen = manipulate(screen)
    #cv2.imshow('window1', new_screen)
    cv2.imshow('Bot', manipulate(np.array(ImageGrab.grab(bbox=(0   , 80, 620, 270)))))

    if np.any(new_screen !=0):
        jump()

    else:
        pass
    #cv2.imshow('Bot', np.array(ImageGrab.grab(bbox=(0,80,620,270))))
    if cv2.waitKey(25) & 0xff == ord('q'):
        cv2.destroyAllWindows()
        break

