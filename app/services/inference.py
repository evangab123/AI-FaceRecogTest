import onnxruntime as ort
import numpy as np
import cv2
from app.core.config import settings

session = ort.InferenceSession(settings.MODEL_PATH)

def preprocess(img: np.ndarray) -> np.ndarray:
    img = cv2.resize(img, (112, 112))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = (img - 127.5) / 128.0
    img = np.transpose(img, (2, 0, 1))  
    return img.astype(np.float32)

def get_face_embedding(img: np.ndarray) -> np.ndarray:
    input_tensor = preprocess(img)[np.newaxis, :]
    outputs = session.run(None, {'input.1': input_tensor})
    embedding = outputs[0][0]
    norm = np.linalg.norm(embedding)
    return embedding / norm  
