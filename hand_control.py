import pyautogui
from collections import deque
from config import DEADZONE, SMOOTHING

pyautogui.FAILSAFE = False


class HandController:
    def __init__(self):
        self.x_buffer = deque(maxlen=SMOOTHING)
        self.left_pressed = False
        self.right_pressed = False
        self.space_pressed = False
        self.state = "CENTER"

    def process(self, lm, frame_w, center_x):
        x = lm[0].x * frame_w
        self.x_buffer.append(x)
        smooth_x = sum(self.x_buffer) / len(self.x_buffer)
        delta = smooth_x - center_x
        
        if delta < -DEADZONE:
            self._press_left()
            self.state = "LEFT"

        elif delta > DEADZONE:
            self._press_right()
            self.state = "RIGHT"

        else:
            self._release_lr()
            self.state = "CENTER"

        one_finger = (
            lm[8].y < lm[6].y and
            lm[12].y > lm[10].y and
            lm[16].y > lm[14].y and
            lm[20].y > lm[18].y
        )

        if one_finger and not self.space_pressed:
            pyautogui.press("space")
            self.space_pressed = True

        if not one_finger:
            self.space_pressed = False

        return smooth_x, self.state, one_finger

    def _press_left(self):
        if not self.left_pressed:
            pyautogui.keyDown("left")
            self.left_pressed = True
        if self.right_pressed:
            pyautogui.keyUp("right")
            self.right_pressed = False

    def _press_right(self):
        if not self.right_pressed:
            pyautogui.keyDown("right")
            self.right_pressed = True
        if self.left_pressed:
            pyautogui.keyUp("left")
            self.left_pressed = False

    def _release_lr(self):
        if self.left_pressed:
            pyautogui.keyUp("left")
            self.left_pressed = False
        if self.right_pressed:
            pyautogui.keyUp("right")
            self.right_pressed = False

    def cleanup(self):
        pyautogui.keyUp("left")
        pyautogui.keyUp("right")
