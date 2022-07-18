import os
import time

import cv2
from dotenv import load_dotenv

import face_recognition

# Configuration
load_dotenv()
PASSWORD = os.getenv("PASSWORD")

faces_location = "./.faces/"

# Load a sample picture and learn how to recognize it.
all_faces = [face_recognition.load_image_file(os.path.join(faces_location, face)) for face in os.listdir(faces_location)]
known_face_encodings = [face_recognition.face_encodings(face)[0] for face in all_faces]
#obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
#known_face_encodings = [obama_face_encoding, ]



def am_i_on_frame(rgb_small_frame):
    """
    Find all the faces and face encodings in the current frame of video
    and find if match with known encodings
    """
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        if True in matches:
            print("you're on screen")
            return True

    print("you're not on screen")
    return False


def main():
    """doc"""
    video_capture = cv2.VideoCapture(0)
    t_end = time.time() + 30
    while time.time() < t_end:
        time.sleep(2)
        _, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        am_i_on_frame(rgb_small_frame)



if __name__ == "__main__":
    main()
