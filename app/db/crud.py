import numpy as np
from sqlalchemy.orm import Session
from app.db.face_model import FaceVector

def regis_face(db: Session, vector: np.ndarray, image_path: str = None):
    vector_bytes = vector.tobytes()
    face = FaceVector(vector=vector_bytes, image_path=image_path)
    db.add(face)
    db.commit()
    db.refresh(face)
    return face

def get_all_faces(db: Session):
    faces = db.query(FaceVector).all()
    return [{"id": face.id, "image_path": face.image_path} for face in faces]


def del_face(db: Session, face_id: int):
    face = db.query(FaceVector).filter(FaceVector.id == face_id).first()
    img = face.image_path if face else None
    if face:
        db.delete(face)
        db.commit()
    return face, img

def cosine_similarity(vec1: np.ndarray, vec2: np.ndarray) -> float:
    dot_product = np.dot(vec1, vec2)
    norm_product = np.linalg.norm(vec1) * np.linalg.norm(vec2)
    return dot_product / norm_product if norm_product != 0 else 0.0

def recog_face(db: Session, target_vector: np.ndarray, threshold: float = 0.4):
    faces = db.query(FaceVector).all()
    for face in faces:
        db_vector = np.frombuffer(face.vector, dtype=np.float32)

        similarity = cosine_similarity(db_vector, target_vector)
        if similarity >= threshold:
            return face
    return None
