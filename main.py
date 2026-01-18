import os, sys

if getattr(sys, "frozen", False):
    exe_dir = os.path.dirname(sys.executable)
    os.chdir(exe_dir)

import cv2
import mediapipe as mp
from game_window import open_game_left
from hand_control import HandController
from camera import draw_debug, move_camera_window

WINDOW_NAME = "Jet Rush Controller"
KEY_ESC = 27

def main():
    print("Đang mở game")
    open_game_left()

    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(
        max_num_hands=1,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.7
    )

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        return

    controller = HandController()
    window_moved = False

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape
        center_x = w // 2

        result = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        if result.multi_hand_landmarks:
            lm = result.multi_hand_landmarks[0].landmark
            smooth_x, state, one_finger = controller.process(lm, w, center_x)
            draw_debug(frame, center_x, h, state, smooth_x, one_finger)

        cv2.imshow(WINDOW_NAME, frame)

        if not window_moved:
            move_camera_window(WINDOW_NAME)
            window_moved = True

        key = cv2.waitKey(1) & 0xFF
        if key == KEY_ESC:
            break

        if cv2.getWindowProperty(WINDOW_NAME, cv2.WND_PROP_VISIBLE) < 1:
            break

    controller.cleanup()
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
