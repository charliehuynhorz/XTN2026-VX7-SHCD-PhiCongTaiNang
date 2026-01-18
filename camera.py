import cv2
import pyautogui
from config import DEADZONE, WEB_RATIO


def move_camera_window(window_name):
    screen_w, _ = pyautogui.size()
    cam_x = int(screen_w * WEB_RATIO) + 10
    cam_y = 20
    cv2.moveWindow(window_name, cam_x, cam_y)


def draw_debug(frame, center_x, h, state, smooth_x, one_finger):
    cv2.line(frame, (center_x - DEADZONE, 0),
             (center_x - DEADZONE, h), (255, 255, 0), 2)
    cv2.line(frame, (center_x + DEADZONE, 0),
             (center_x + DEADZONE, h), (255, 255, 0), 2)
    cv2.line(frame, (center_x, 0),
             (center_x, h), (0, 255, 255), 1)

    cv2.putText(frame, state, (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

    if one_finger:
        cv2.putText(frame, "SPACE", (10, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

    cv2.circle(frame, (int(smooth_x), h // 2), 10, (0, 255, 0), -1)
