from fastapi import FastAPI, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
import numpy as np
import cv2
from app.db.session import SessionLocal
from app.db.crud import regis_face, get_all_faces, del_face, recog_face
from app.services.inference import get_face_embedding
import shutil
import os

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/face")
def get_faces(db: Session = Depends(get_db)):
    return get_all_faces(db)

@app.post("/api/face/register")
def register_face(file: UploadFile = File(...), db: Session = Depends(get_db)):
    contents = file.file.read()
    np_arr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    
    if img is None:
        return {"status": "error", "message": "Invalid image format"}

    embedding = get_face_embedding(img)
    saved_path = f"static/{file.filename}"
    os.makedirs("static", exist_ok=True)
    with open(saved_path, "wb") as buffer:
        buffer.write(contents)

    face = regis_face(db, embedding, saved_path)
    return {"id": face.id, "image_path": face.image_path}

@app.post("/api/face/recognize")
def recognize_face(file: UploadFile = File(...), db: Session = Depends(get_db)):
    contents = file.file.read()
    np_arr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    
    if img is None:
        return {"status": "error", "message": "Invalid image format"}

    embedding = get_face_embedding(img)
    match = recog_face(db, embedding)
    if not match:
        return {"status": "error", "message": "No matching face found"}
    return {"id": match.id, "image_path": match.image_path}

@app.delete("/api/face/{face_id}")
def delete_face(face_id: int, db: Session = Depends(get_db)):
    face, image_path = del_face(db, face_id)
    if image_path and os.path.exists(image_path):
        os.remove(image_path)
    if not face:
        return {"status": "error", "message": "Face not found"}
    return {"detail": f"Face ID {face_id} deleted"}
