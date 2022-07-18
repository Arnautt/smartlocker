import os

import face_recognition


def get_known_encodings(images_path):
    """doc"""
    all_faces = [face_recognition.load_image_file(os.path.join(images_path, face)) for face in
                 os.listdir(images_path)]
    known_face_encodings = [face_recognition.face_encodings(face)[
        0] for face in all_faces]
    return known_face_encodings


def am_i_on_frame(rgb_small_frame, known_face_encodings):
    """
    Find all the faces and face encodings in the current frame of video
    and find if match with known encodings
    """
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(
        rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(
            known_face_encodings, face_encoding)
        if True in matches:
            return True

    return False
