import os
import time

import cv2
from dotenv import load_dotenv

from src.recognition import am_i_on_frame, get_known_encodings
from src.utils import Computer

# Configuration
load_dotenv()
PASSWORD = os.getenv("PASSWORD")
SLEEPING_TIME = int(os.getenv("SLEEPING_TIME"))
FACES_LOCATION = os.getenv("FACES_LOCATION")


def main():
    """doc"""
    computer = Computer()
    known_face_encodings = get_known_encodings(FACES_LOCATION)
    video_capture = cv2.VideoCapture(0)

    process_this_frame = True
    t_end = time.time() + 30
    while time.time() < t_end:
        time.sleep(SLEEPING_TIME)
        _, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        if process_this_frame:
            on_frame = am_i_on_frame(rgb_small_frame, known_face_encodings)
            if on_frame:
                if computer.is_locked():
                    print("Computer is locked and you're on frame: unlocking.")
                    computer.unlock(PASSWORD)
                else:
                    print(f"On frame but not locked: sleep {SLEEPING_TIME} seconds.")

            else: # not on frame
                if computer.is_locked():
                    print(f"Not on frame and computer locked : sleep {SLEEPING_TIME} seconds.")
                else:
                    print("Not on frame and computer not locked : locking computer.")
                    computer.lock()

        process_this_frame = not process_this_frame


if __name__ == "__main__":
    # TODO :
    #  ajouter les reqs
    #  tests unitaires + mlops
    main()
