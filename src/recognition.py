import os

import face_recognition


def get_known_encodings(images_path):
    """
    Get all known face encodings

    Parameters
    ----------
    images_path: str
        Path where your face image are stored

    Returns
    -------
    known_face_encodings: list
        All know face encodings
    """
    all_faces = []
    for face in os.listdir(images_path):
        try:
            new_face = face_recognition.load_image_file(os.path.join(images_path, face))
            all_faces.append(new_face)
        except:
            pass
    known_face_encodings = [face_recognition.face_encodings(face)[
        0] for face in all_faces]
    return known_face_encodings


def am_i_on_frame(rgb_small_frame, known_face_encodings):
    """
    Find all the faces in the current frame of video and test if match with known encodings

    Parameters
    ----------
    rgb_small_frame: np.array
        Frame from the video
    known_face_encodings: list
        All known face encodings
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
