from sqlalchemy import Column, Integer, String, LargeBinary
from app.db.session import Base

class FaceVector(Base):
    __tablename__ = "face_vectors"

    id = Column(Integer, primary_key=True, index=True)
    image_path = Column(String, nullable=True)
    vector = Column(LargeBinary, nullable=False)
    
