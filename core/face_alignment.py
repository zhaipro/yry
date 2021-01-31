import os
import dlib
from pathlib import Path
root_path = Path(__file__).parent


class LandmarksDetector:
    def __init__(self, predictor_model_path):
        """
        :param predictor_model_path: path to shape_predictor_68_face_landmarks.dat file
        """
        self.detector = dlib.get_frontal_face_detector() # cnn_face_detection_model_v1 also can be used
        self.shape_predictor = dlib.shape_predictor(predictor_model_path)
        self.threshold = 0

    def get_landmarks(self, img):
        if isinstance(img, str):
            img = dlib.load_rgb_image(img)
        dets, scores, idx = self.detector.run(img, 1, 0)  # The seconde param always be 1, which means upsample the image 1 time,
                                                            # this will make everything bigger and allow us to detect more faces.
                                                            # The third param is score.

        for i, detection in enumerate(dets):
            try:
                if scores[i] < self.threshold:
                    continue
                # print(f'image: {image}   i:{i}   score: {scores[i]}')
                face_landmarks = [(item.x, item.y) for item in self.shape_predictor(img, detection).parts()]
                yield face_landmarks
            except Exception:
                print("Exception in get_landmarks()!")


landmarks_model_path = os.path.join(root_path, 'shape_predictor_68_face_landmarks.dat')
landmarks_detector = LandmarksDetector(landmarks_model_path)
