import cv2
import os
from dotenv import load_dotenv

# Configuration
load_dotenv()
faces_location = os.getenv("FACES_LOCATION")
n_picture = 0
video_capture = cv2.VideoCapture(0)

print("Start generating pictures for face recognition\n",
      "Press 'p' to take a picture.\n",
      "Press 'q' to quit.")

# Main loop to take arbitrary N pictures
while True:
    ret, frame = video_capture.read()
    cv2.imshow('Video', frame)
    k = cv2.waitKey(1)

    if k == ord('q'):
        break
    elif k == ord('p'):
        _path = os.path.join(faces_location, f"picture_{n_picture}.png")
        cv2.imwrite(_path, frame)
        n_picture += 1
    else:
        pass


print(f"Done. Took {n_picture} pictures.")
video_capture.release()
cv2.destroyAllWindows()
