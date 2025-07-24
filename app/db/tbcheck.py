from session import SessionLocal
from app.db.face_model import FaceVector

db = SessionLocal()

# Uji insert face vector dummy
import numpy as np
dummy_vec = np.random.rand(128).astype(np.float32)

from crud import regis_face
face = regis_face(db, dummy_vec, "test.jpg")
print("Inserted face ID:", face.id)
